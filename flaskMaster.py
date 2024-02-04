from flask import Flask, render_template, request, jsonify
import locateaddress as la
import os
from LifeLink import LifeLink

path = os.environ.get('Hospital App')

app = Flask(__name__, template_folder='/Users/Arush/SALS/VikingsHack/templates')
app.secret_key = 'password'
global distance
distance = 0

def locations():
    i = LifeLink()
    i.get_current_location()
    i.get_nearby_places()
    

@app.route('/')
def home():
    return render_template('homepage.html') + "<h3>Closest Address Determined: <h3>" \
    + f"<h2>{la.address_finder()}</h2>" + "<hr>" + \
    render_template('map.html') + "<h2>Fremont Urgent Care (30 min)</h2>" \
    + "<h2>AED Urgent Care (97 min)</h2>" + "<h2>Sutter Health Urgent Care (103 min)</h2>" + \
    "<h2>American Expert Doctors (120 min)</h2>"

@app.route('/process-data', methods=['POST'])
def process():
    data = request.json['data']
    with open('initialize.txt', 'w') as f:
        f.write(data)
        f.write('\nurgent care')
    print(data)
    return jsonify({'result': data})

if __name__ == '__main__':
    app.run(debug=True)