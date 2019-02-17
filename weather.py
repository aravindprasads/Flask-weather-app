import requests
from flask import Flask, render_template as rt, request
import json                                                                                         
import re                                                                                         
import urllib2                                                                                      
import os                                                                                           
import subprocess                                                                                   
                    
app = Flask(__name__)
app.config['DEBUG'] = True
file_name = "downloaded_city_names"
file_name_gz = file_name + ".gz"
output_file = "user_entries"

## Function to download the City info from the Openweathermap website.
def download_file():
    if (os.path.isfile(file_name) != True):                                                       
        dn_file = urllib2.urlopen("http://bulk.openweathermap.org/sample/city.list.json.gz")

        with open(file_name_gz,'wb') as output:                                                   
            output.write(dn_file.read())                                                                
        
        if (os.path.isfile(file_name_gz) == True):                                                
            bashCommand = "gunzip " + file_name_gz
            output = subprocess.check_output(['bash','-c', bashCommand])
    
## Function to create the output file in local directory 
def create_output_file():
    bashCommand = "touch " + output_file
    output = subprocess.check_output(['bash','-c', bashCommand])

## Function to create the dictionary with City-names for validations of user input
def make_name_dict():
    cities_dic = {}
    cities_list = []
    reg = re.compile("(\b\"name\"\: \")(\w\s*\w*)(\"\,)") 
    with open(file_name) as f:                                                                   
        lines = f.readlines()                                                                           
    for line in lines:
        line = line.rstrip('\n')
        match = re.search('(\s+\"name\"\: \")([\w\s]+)(\"\,)', line)
        if match:
            c = match.group(2)
            cities_dic[c] = 1
            cities_list.append(c)
    return cities_dic, cities_list

## Function to check if the user provided City is present in already created dictionary
def check_city(city_dic, new_city):
    if new_city in city_dic:
        return True
    return False    

## Main page
@app.route('/', methods=['GET', 'POST'])
def index():
    download_file()
    create_output_file()
    city_dic, cities_list = make_name_dict()
    cities = []
    file_dic = {}

    fp = open(output_file,"r") 
    lines = fp.readlines()
    for line in lines:
        line = line.rstrip('\n')
        cities.append(line)
        file_dic[line] = 1
    fp.close()

    if [request.method == 'POST']:
        new_city = request.form.get('city')
        if new_city:
            if (check_city(city_dic, new_city) == True):
                if new_city not in file_dic:
                    fp = open(output_file,"a")
                    fp.write(new_city+"\n")
                    cities.append(new_city)
                    fp.close()
            else:
                error_str = "<b>" + "\"" + new_city + "\" "+ "</b>"
                error_str += """City Name is not supported curently.
                              Only the following Cities are supported (Case sensitive)""" 
                cities_list_str = ""
                for x in range(len(cities_list)):
                    cities_list_str += "<b>" + str(cities_list[x]) + "</b>" + "<br/>"
                return (error_str + "<br/><br/>" +cities_list_str)

        del_city = request.form.get('city_delete')
        if del_city:
            if del_city in cities:
                cities.remove(del_city)
                fp = open(output_file,"w")
                for x in range(len(cities)):
                    fp.write(cities[x]+"\n")

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=<app-key-id>'
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        weather = {
            'city' : r['name'],
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],        
            'icon' : r['weather'][0]['icon']
        }
        weather_data.append(weather)
    return rt('weather.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run()
