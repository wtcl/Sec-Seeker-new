import requests
import json
from bd09lltobd09mc import bd09tomercator


header = {"use-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
          }


def getbd(gps):
    url = "https://api.map.baidu.com/geoconv/v1/?coords={}&from=1&to=5" \
          "&ak=B13d386658b7f5e9c2e2294e0314afbe" \
          "&callback=BMap._rd._cbk15189" \
          "&seckey=75%2BuHWwjjfW9wPxhq4Cdbd3AYS%2FdfnPS9sCmkM6vgvc%3D%2C8U" \
          "DrgZnn8ZbbtXJqQTDMYp8MZ0gXhZbl6bb182gGV01JIoQH_8dw8LrKOvNBlD_zHI" \
          "aMlNYfU0lC5aZ8BIW1u39BSHd33JW6HCwuVVmAJBBohHLxIqqvI3d1LZgNkf5SEU" \
          "mAhxNFHc0Z-o2bo09A5msp8sL8t97BQj-mMWwcH9o6aVKmEU8ujp4uEIyTK5Wr" \
          "&timeStamp=1648272076478&sign=304396e4a8d2".format(gps)
    html = requests.get(url, headers=header)
    content = html.text.split("(")[-1][:-1]
    content = json.loads(content)["result"][0]
    bd = [content["x"], content["y"]]
    # print(bd)
    return bd


def getsite(x, y):
    url = "https://api.map.baidu.com/?qt=rgc&x={}&y={}&dis_poi=100" \
          "&poi_num=10&latest_admin=1&ie=utf-8&oue=1&fromproduct=jsapi" \
          "&v=2.1&res=api&callback=BMap._rd._cbk19690&ak=E4805d16520de" \
          "693a3fe707cdc962045&seckey=75%2BuHWwjjfW9wPxhq4CdbXvQvvLt2G" \
          "o3%2FLOEKiPH4to%3D%2C8UDrgZnn8ZbbtXJqQTDMYkLakLYkMDkwS7X-__" \
          "EFScZJxd3CXWaj7wjXaqPB2FM2j74SiEifzAXSX1a-C9BwJwSUfH5k-2JM2N" \
          "TpxysEjNHkwbHv54hSEihugHKb6uNoJPDJSWnjJzpCS2FAHjvzusuaEEZRUo" \
          "Iwc_X74nXyJsFUuKP8g9cHF0rPcKbIBmyn&timeStamp=1648271309331" \
          "&sign=b46f801a1ab3".format(str(x), str(y))
    html = requests.get(url, headers=header)
    con = json.loads(html.text[45:-1])
    site = con["content"]["poi_desc"]
    return site


def gpstolocation(gps):
    bd = getbd(gps)
    mercator = bd09tomercator(bd[0], bd[1])
    print(mercator)
    position = getsite(mercator[0], mercator[1])
    # print(position)
    return position


if __name__ == "__main__":
    gps = "108.84,34.15"
    bd = getbd(gps)
    print(bd09tomercator(bd[0], bd[1]))
    gps = "108.841,34.151"
    bd = getbd(gps)
    print(bd09tomercator(bd[0], bd[1]))
    print(gpstolocation("108.25,34.12"))
