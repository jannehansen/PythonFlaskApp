# -*- coding: utf-8 -*-

#############################################
# PUBLISH SAMPLE FLASK APPLICATION
# IN AZURE WEB APP FOR CONTAINERS
#############################################
# This is just simplest helloworld + API
# application written in python
# using flask
#############################################
# (c) Janne Hansen 2018, MIT LICENCE
#############################################

#imports
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template

# for the api
import json

import logging

#############################################
# FLASK STUFF
#############################################

app = Flask(__name__)

# Just that we have a start page for the web application
@app.route("/")
def hello():
    
    # https://www.tutorialspoint.com/flask/flask_templates.htm
    app.logger.info("hello called")

    return render_template("hello.html"),200

# The api method. Expects a parameter named "input"
@app.route("/api")
def api():

    retdict ={} 

    try:
        input_string = request.args.get("input","[you forgot to feed in input]")
        app.logger.info("FAKE API CALL, input = "+input_string)

        response = {
            'input':input_string,
            'my_api_output':"hello api "+input_string
        } 
        
        retdict['response']=response

    except Exception as e:
        msg = "Bad Request (400): "+str(e)
        app.logger.info(msg)
        # print(msg)
        return msg,400
    
    retJson = str(retdict).replace('\'','"')
    app.logger.info("retjson :"+retJson)

    resp = make_response(retJson)
    resp.headers['content-type']="application/json"

    # http://www.flaskapi.org/api-guide/status-codes/#successful-2xx
    return resp, 200

#############################################
# MAIN
#############################################

if __name__=='__main__':

    # Set the logger level
    app.logger.setLevel(logging.INFO)

    # And now to work
    app.logger.info("PythonFlaskApp starting....")

    # If you had something to initialize before we start the server
    # this would be the place to do just that.

    # Run the flask app
    # Flask app default port is 5000
    app.run(debug=True,host='0.0.0.0')

    app.logger.info("PythonFlaskApp Finished.")

#############################################
# END OF FILE
#############################################
