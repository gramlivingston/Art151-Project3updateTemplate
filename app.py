from flask import Flask, render_template, request, jsonify, redirect
import time
from random import randint
import requests

#Make a list of the lattitudes and longitudes
lat = [0]
lng = [0]


app = Flask(__name__)

#since we are just returning a jsonified dictionary and not a usable html page, we don't need to make an imgandtitle html file
@app.route('/left', methods=['GET', 'POST'])
def apiCall():
  
  #Get the Last item in the Latitude List and add to it
    newLat = lat[-1] + 1
  #Get the most recent longitude
    longitude = lng[-1]

  #Append the most recent Latitude to the Latitude list so that you can get it on the next call
    lat.append(newLat)

  #Do the api call with the newLat and return a new image url
    url = f'{newLat}/{longitude}'


    Data = {
        'url': url

    }

    #return your json file

    return jsonify(**Data)   




@app.route('/up', methods=['GET', 'POST'])
def upCall():
  
  #Get the Last item in the Latitude List and add to it
    newLng = lng[-1] + 1

  #Get the most recent longitude
    latitude = lat[-1]
  #Append the most recent Latitude to the Latitude list so that you can get it on the next call
    lng.append(newLng)

  #Do the api call with the newLat and return a new image url
    url = f'{latitude}/{newLng}'


    Data = {
        'url': url

    }

    #return your json file

    return jsonify(**Data)   
    


@app.route('/', methods = ['GET', 'POST'])

#define app function

def index():
    Hello = "Hello World!"
    value = randint(0, 100)
        
    url = f'https://picsum.photos/{value}'
       
    print(url)
    Data = {
        'title' : Hello,
        'img' : url
    }

    return render_template('index.html', **Data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)