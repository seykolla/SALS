from flask import Flask, render_template, request, jsonify
import locateaddress as la
import os

path = os.environ.get('Hospital App')

app = Flask(__name__, template_folder='/Users/Arush/SALS/VikingsHack/templates')
app.secret_key = 'password'
global distance
distance = 0

@app.route('/')
def home():
    return render_template('homepage.html') + f"<h3>Closest Address Determined: <h3>" \
        + f"<h2>{la.address_finder()}</h2>" + render_template('button.html') + \
        "<hr>" + render_template('map.html')

@app.route('/process-data', methods=['POST'])
def process():
    data = request.json['data']
    with open('initialize.txt', 'w') as f:
        f.write(data)
    print(data)
    return jsonify({'result': data})

if __name__ == '__main__':
    app.run(debug=True)