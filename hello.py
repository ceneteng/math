from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello(name='chris'):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run('192.168.1.20')
