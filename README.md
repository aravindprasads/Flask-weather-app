# Weather App with Flask

Its a simple Web-App that shows weather info of the cities. Users have options to add/delete their interested cities by providing the City names.

Instructions to run the App:
--
1) Download all files to local directory. 
2) Get the App-key from Openweathermap website (Need to register in website and get the key).
3) Replace the key in weather.py file, line number - 93.
4) Run the weather.py file - "python weather.py".


Live Deployment:
--
This Web-app is deployed at https://aravindprasad.pythonanywhere.com/ 


Snapshot:
--
https://github.com/aravindprasad90/Flask-weather-app/blob/master/Screenshot.png 


Note
--
1) On the first load, there could be some delay since a file of size around 29MB is downloaded from Openweathermap website(https://openweathermap.org/). 
2) This file will be downloaded only once on first load and subsequent usages/refreshes will not perform any downloading tasks and the downloaded file will be re-used up from then on. 


How it Works:
--
1) The weather info is retreived from Openweathermap website(https://openweathermap.org/). 
2) First, the info of all cities is downloaded to local directory (Downloded file will be in gzip format and it is unzipped to get the file). 
3) This is required to check if the value entered by User is valid.
4) An Output file ("user_entries") is maintained as Local DB for the cities added by User.
5) For each city added by User, Checks are made for validity from the downloaded file and duplciate checks are made beofre writing to the "user_entries" file. 
6) The on, all the city names from User_entries file is retreived and the weather info is retreived via APIs provided by Openweathermap site. 
7) The values are passed to the CSS file (in templates directory) for rendering.

Credits:
--
For developing this App, referred to the youtube video - "https://www.youtube.com/watch?v=lWA0GgUN8kg".

Additions on top of the features in Video:
--
1) Added Option for Users to delete the Citynames from displayed info UI.
2) Downloaded the City info from the Openweathermap website for local validation.
3) Added validity checks for City Names provided by User (using the downloaded file from website)
4) Used Local Files instead of SQLDB for simplicity. Also, the motive of this App is to learn flask and hence, avoided the complexities of SQLDB code.
5) Duplicate checks made before adding to Citynames to Local DB File.

Basic Guidelines for working on Flask:
--
I) Always use virtualenv/virtualenv wrapper packages for the Flask projects. This is basically to create an isolated environment for the project and the packages downloaded will not affect rest of the libraries in system. 

Steps for creating Virtualenv:
--
1) pip install virtualenv
2) pip install virtualenvwrapper 
3) In Bash file ==> "export WORKON_HOME=~/.virtualenvs; source /usr/local/bin/virtualenvwrapper.sh"
4) Create a directory for project and goto directory. 
5) Create the virtual env ==> "mkvirtualenv -a $(pwd) name-of-env"
(This will help to map the virtual enviromnment to the path location)
6) To start wroking on virtual env ==> workon name-of-env
7) For deleting the virtualenv, "rmvirtualenv name-of-env"
8) For viewing the list of packages in virtual env, "pip list"

