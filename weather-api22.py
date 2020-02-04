from flask import request , Flask
import json
import requests
app = Flask(__name__)
@app.route("/city_weather/", methods=['GET'])
def weather_city ():
    c = request.args.get('city',default=None, type=str)
    res = ""
    if c:
        key = "62609e64d9ce42749db03230200402"
        url = "http://api.worldweatheronline.com/premium/v1/weather.ashx?"
        name = request.args.get('city', default=None, type=str)
#         if name == 'e':
#             break
        params = {
        "key" : key,
        "q":name,
        "format":'json',
        "num_of_days":5
        }
        res = requests.get(url, params=params)
        res = json.loads(res.text)
        k = res["current_condition"]
        res = "<h1> Weather of {} = {} </h1>".format(c,k)
    else:
        res = "<h1>No city found </h1>"
    return res
@app.route('/')
def index():
    return "Home Page"
if __name__ == "__main__":
    app.run(debug=True)
