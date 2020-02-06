from flask import request , Flask
import json
import requests
app = Flask(__name__)
@app.route("/city/", methods=['GET'])
def weather_city ():
    c = request.args.get('name',default=None, type=str)
    res = ""
    if c:
        key = "49cd3ff9fc6d4e7f1f2caeaaf7715a3b"
        url = "https://samples.openweathermap.org/data/2.5/weather?"
        params = {
        "appid":key,
        "q":c
        }
        res = requests.get(url, params=params)
        res = json.loads(res.text)
        k = res['main']['temp']
        res = "<h1> Weather of {} = {} </h1>".format(c,k)
    else:
        res = "<h1>No city found </h1>"
    return res
@app.route('/')
def index():
    return "Home Page"
if __name__ == "__main__":
    app.run(debug=True) 
