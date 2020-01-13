import urllib.request

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()
print('type(data) = ', type(data))

text = data.decode('utf-8')
print(text)