from flask import Flask, render_template
import os

path = os.environ.get('Hospital App')

app = Flask(__name__, template_folder='/Users/Arush/VikingsHack/templates')
app.secret_key = 'password'

@app.route('/')
def home():
    return render_template('export.html')

if __name__ == '__main__':
    app.run(debug=True)