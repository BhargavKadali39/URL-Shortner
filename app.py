from flask import Flask,render_template,request
import pyshorteners as sh

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/result", methods=['get','post'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    link = name
    s = sh.Shortener()
    x = (s.tinyurl.short(link))
    return render_template('index.html',tinyy=x)
if __name__ == '__main__':
    app.run()
