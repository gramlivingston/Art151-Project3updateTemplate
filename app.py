from flask import Flask, render_template, request, jsonify, redirect
#import RPi.GPIO as GPIO
import time
from random import randint
import requests



app = Flask(__name__)

#since we are just returning a jsonified dictionary and not a usable html page, we don't need to make an imgandtitle html file
@app.route('/imgandtitle', methods=['GET', 'POST'])
def apiCall():
  

    value = randint(0, 100)
    #random photo url could 
    base_url = f'https://picsum.photos/{value}'
       
    #Since we are replacing an attribute all we need to do is get the new url as a string.
    url = base_url
    #use full h2 tag since you're replacing the html object with a new one
    title = f'<h2 id=title >{value}</h2>'

    Data = {
        'url': url,
        'title': title

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
    app.run(host='0.0.0.0', port=80, debug=False)