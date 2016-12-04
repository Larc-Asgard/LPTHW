from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello World"
    render = render_template('foo.html', greet_no_exist = greeting)
    #Simple to put: the greet variable no longer exist here so that the if test
    #in the HTML file would return false
    return render

if __name__ == '__main__':
    app.run()
