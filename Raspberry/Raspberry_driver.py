from flask import Flask, request, jsonify
import requests
import json
import schedule

app = Flask(_name_)

weight = 150
AQI= 400

@app.route("/")
def home_view():
    return "<h1>Hi, I am bin 75462</h1>"

@app.route("/check")
def check():
    aqi = int(request.args.get('aqi'))
    wght = int(request.args.get('wght'))
    checker(aqi, wght);
    return "this bin is checked now!"

def regisComplaint():
    r = requests.post("https://localhost:8000/complaint", 
    data={"address": "in front of something",
        "location":"[85.2627,20.8564]",
        "complaint":"garbage overflow",
        "binID":"123456"},
        )

    print(r)    

def checker(aqi, wght):
    if aqi > 500 or wght > 200:
        regisComplaint()

schedule.every().hour.do(checker) 

if _name_ == '_main_':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)