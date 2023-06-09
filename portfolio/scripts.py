from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('elements.html')

if __name__=='__main__':
    app.run(debug = True,host="0.0.0.0")

@app.route('/static/<path:path>')
def static(path):
    return send_from_directory('static', path)