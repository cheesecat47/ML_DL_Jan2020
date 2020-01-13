#모듈 로딩 --------------------------------------
import sqlite3

# 데이터 변수 선언 -------------------------------
filepath = "test2.sqlite"

# 데이터베이스 제어 ------------------------------ 
# (1) 데이터베이스 연결
conn = sqlite3.connect(filepath)

# (2) 테이블생성및데이터넣기
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items") 
cur.execute("""CREATE TABLE items (
    item_id INTEGER PRIMARY KEY, 
    name TEXT,
    price INTEGER)""")

# (3) 변경내용적용
conn.commit()


# 데이터 넣기 ------------------------------------- 
# (1) 데이터베이스 접근 포인트(커서) 획득
cur = conn.cursor()

# (2) 데이터 삽입
cur.execute(
    "INSERT INTO items (name,price) VALUES (?,?)", 
    ("Orange", 5200))

# (3) 변경내용적용
conn.commit()


# 여러 데이터 연속으로 넣기 ----------------------------- 
# (1) 데이터베이스 접근 포인트(커서) 획득
cur = conn.cursor()

# (2) 데이터 리스트
data = [("Mango",7700), ("Kiwi",4000), ("Grape",8000), 
    ("Peach",9400),("Persimmon",7000),("Banana", 4000)]

# (3) 데이터 한 번에 여러 개 넣기
cur.executemany(
    "INSERT INTO items(name,price) VALUES (?,?)", 
    data)

# (4) 변경정보설정
conn.commit()

# 4000-7000원 사이의 데이터 추출
cur = conn.cursor() 
price_range = (4000, 7000) 
cur.execute(
    "SELECT * FROM items WHERE price>=? AND price<=?", price_range)
fr_list = cur.fetchall() 
for fr in fr_list:
    print(fr)