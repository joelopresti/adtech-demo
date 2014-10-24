from flask import Flask, render_template, redirect, url_for, jsonify
from app import app
import requests



@app.route('/')
@app.route('/index')
def index():

    h = requests.get('http://www.scientiamobile.com/site/header')
    header = h.text
    f = requests.get('http://www.scientiamobile.com/site/footer')
    footer = f.text
    return render_template('index.html', header=header, footer=footer)


@app.route('/wurfl_meme/<form_factor>/<text>')
def meme(form_factor, text):

    text1 = "I don't always use a %s" % form_factor
    text2 = "But when I do, it's a %s" % text
    u = 'https://api.imgflip.com/caption_image'
    payload = {'template_id': '61532', 'username': 'fendermaniac', 'password': 'bichon', 'text0': text1, 'text1': text2}
    r = requests.post(u, params=payload)

    return jsonify(**r.json())