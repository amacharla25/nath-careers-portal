from flask import Flask,render_template

app = Flask(__name__)

@app.route("/") #route is the part of the url - its a decorator
def hello():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)