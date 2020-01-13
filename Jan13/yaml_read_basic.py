# 모듈 로딩 ---------------------------------------- yaml_read_basic.py
import yaml
# 데이터 변수 선언 ----------------------------------
yaml_str = """ 
Date: 2017-03-10 
PriceList:
    -
        item_id: 1000 
        name: Banana 
        color: yellow 
        price: 800
    -
        item_id: 1001 
        name: Orange 
        color: orange 
        price: 1400
"""

# YAML 분석 -------------------------------------------
data = yaml.load(yaml_str, Loader=yaml.FullLoader)

# 이름, 가격 데이터 출력 --------------------------------
for item in data['PriceList']:
    print(item["name"], item["price"])
