import asyncio
import json
import pandas as pd
import requests
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import config
from search_cloud import pandas_new_search_id, place_search, \
    search_relationships

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


# class TrackData(db.Model):
#     __tablename__ = 'track_data'
#     ssid = db.Column(db.String(100),
#                      unique=False, index=True, primary_key=True)
#     t = db.Column(db.Integer(), unique=False)
#     x = db.Column(db.Integer(), unique=False)
#     y = db.Column(db.Integer(), unique=False)
#
#     def __repr__(self):
#         return self.ssid


@app.route("/")
def hello_world():

    return "Hello World! Here is the cloud!"


@app.route("/api", methods=["POST"])
def upload():
    print(request.data)
    # print("接收到来自"+json.loads(request.data)["con"].split(",")[1]+"的数据")
    # print("数据存储完成")
    # track = json.loads(request.data)["track"]
    # track = track.split(",")
    # key = json.loads(request.data)["key"]
    # placeid = requests.post(json.dumps({"treeid": track[-1]}))
    # if key == "EEEEEE" and placeid != "hack":
    #     track[-1] = str(int(placeid, 16))
    #     track = ",".join(track)
    #     info = track+"\n"
    #     with open("static/data/dbtrack.txt", "a+") as f:
    #         f.write(info)
    #     return "Yes"
    # else:
    #     return "hack!"
    return "1"


@app.route("/idsearch", methods=["POST"])
def search_id():
    if json.loads(request.data)["role"] == "admin":
        print("开启查询风险者")
        uuid = json.loads(request.data)["uuid"]
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print("start")
        result = pandas_new_search_id(uuid)
        print("查询结果如下：\n", result)
        return "<br>".join(result)
    else:
        return "hack"


@app.route("/placesearch", methods=["POST"])
def search_place():
    starttime = json.loads(request.data)["starttime"]
    endtime = json.loads(request.data)["endtime"]
    treeid = json.loads(request.data)["treeid"]
    area = json.loads(request.data)["area"]
    print("接收到查询请求，开启查询")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = place_search(int(starttime), int(endtime), treeid, area)
    print("查询结果如下:\n", result)
    return "<br>".join(result)


@app.route("/relasearch", methods=["POST"])
def rela_search():
    names = json.loads(request.data)["uuids"]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    print("接收到查询请求，开启查询")
    result = search_relationships(names)
    print("查询结果如下：\n", result)
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True, threaded=True)
