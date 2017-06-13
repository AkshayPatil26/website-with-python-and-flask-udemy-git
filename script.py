
app=Flask(__name__)

@app.route('/')
def home():

@app.route('/about')
def about():


if __name__=="__main__":
    app.run (debug=True) #if this script is run; not if script is imported elsewhere
