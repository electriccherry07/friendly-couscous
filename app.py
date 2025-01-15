from flask import Flask
from flask import render_template,request

app = Flask(__name__) #confirm the application belongs to you

@app.route("/")
def index():
    return(render_template("index.html"))

if __name__ == "__main__": #reconfirm
    app.run()
