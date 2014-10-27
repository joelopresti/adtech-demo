from flask import Flask, request, render_template, redirect, url_for, jsonify
from app import app
from wurfl_cloud import Cloud as WurflCloud
from wurfl_cloud import utils
import requests
import json



@app.route('/')
@app.route('/index')
def index():
    # Client UA
    ua = request.headers.get('User-Agent')

    # Cloud client stuf
    config = utils.load_config('/home/joe/code/python/adtech-demo/app/filecache_config.conf')
    cache = utils.get_cache(config)
    client = WurflCloud(config, cache)
    device = client(ua, capabilities=["resolution_height", "resolution_width"])

    

    user_agent = {'User-agent': ua}
    title = "ad:tech 2014"
    h = requests.get('http://www.scientiamobile.com/site/header', headers=user_agent)
    switch = h.text
    h1 = switch.replace('<a href="/', '<a href="http://www.scientiamobile.com/')
    header = h1.replace('src="/', '<img src="http://www.scientiamobile.com/')

    f = requests.get('http://www.scientiamobile.com/site/footer', headers=user_agent)
    f1 = f.text
    fswitch = f1.replace('<a href="/', '<a href="http://www.scientiamobile.com/')
    footer = fswitch.replace('src="/', '<img src="http://www.scientiamobile.com/')
    return render_template('index.html',title=title, header=header, footer=footer, device=device)


@app.route('/wurfl_meme/<form_factor>/<text>')
def meme(form_factor, text):

    text1 = "I don't always use a %s" % form_factor
    text2 = "But when I do, it's a %s" % text
    u = 'https://api.imgflip.com/caption_image'
    payload = {'template_id': '61532', 'username': 'fendermaniac', 'password': 'bichon', 'text0': text1, 'text1': text2}
    r = requests.post(u, params=payload)

    return jsonify(**r.json())