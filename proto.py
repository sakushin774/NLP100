import sys
import codecs
import json
import re
import urllib.parse
import urllib.request
import MeCab
from PIL import Image

#JSONデータを取得
url = "https://api.prtimes.tech/list/1"
request = urllib.request.Request(url)
connection = urllib.request.urlopen(request)
data = json.loads(connection.read())

#画像データを保持するハッシュ
images = {}

for i in range(0,4):
    #画像のURLにアクセス
    imurl = data['data'][i]['main_image']
    imrequest = urllib.request.Request(imurl)
    imconnection = urllib.request.urlopen(imrequest)

    #画像を表示
    im = Image.open(imconnection)
    im.show()

    # 画像をハッシュに保存
