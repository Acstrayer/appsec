# Application Security Week 1 Simple Flask Application

## Running the Application

The virtual environment that I chose for this application is Python's
virtualenv, since I like that the dependencies are stored in the folder that the
project is held. To run the Application, begin by cloning the repository to your
local system. Once the repository has been cloned, navigate to the directory
'flaskapp1' and in your terminal type source ./bin/activate which will start the
virtual environment with all dependencies included. I'd recommend to then, in
your terminal, type python3 which will open a python3 interpreter in your
terminal which will allow you to type import flask from Flask. If this command
doesn't give an error then the virtualenv was started properly, when you're done
type exit().  
 Once you've confirmed the environment has been initialized properly, type flask
run which will launch the app. If the app does not launch, in your terminal type
export FLASK_APP=app.py and then try flask run again. Once the app is running,
go to your browser of choice and type localhost:5000 into the url bar and press
enter. The simple application should now be running in your web browser. At the
moment, the app can only be used by typing text into the text box then pressing
submit, which will just show the text that was entered into the text box on a
new screen in the browser.

## Barriers and Solutions

The largest barrier I had, surprisingly, was getting the stylesheet to properly
load into the flask application. My solution was to create a 'static' directory
in the project folder, move the style sheets to ./static/stylesheets/\* then
adjusting the link for the style sheets in index.html to load from the static
directory. Setting up simple routes and form handling in flask is fairly
straight forward, so thankfully I didn't have any other major barriers.
