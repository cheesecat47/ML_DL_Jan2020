# 모듈로딩-------------------------------------------- read_json_02.py
import urllib.request as req
import os.path
import json

# 번수 선언 -------------------------------------------
url = "https://api.github.com/repositories"
savename = "./repo.json"

# WEB 데이터 json 파일 다운로드 -------------------------
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# JSON 파일 분석 ---------------------------------------
items = json.loads(open(savename, "r", encoding="utf-8").read())

# JSON 파일 출력 --------------------------------------
for item in items:
    print(item["name"] + " - " + item["owner"]["login"])