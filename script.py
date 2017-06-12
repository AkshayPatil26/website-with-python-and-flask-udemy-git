from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "homepage here!"

@app.route('/about')
def about():
    return "about website blah blah"

if __name__=="__main__":
    app.run (debug=True)
