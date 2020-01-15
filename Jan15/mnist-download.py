import urllib.request as req
import gzip
import os
import os.path

DEBUG = True

savepath = './mnist'
baseurl = 'http://yann.lecun.com/exdb/mnist'
files = [
    'train-images-idx3-ubyte.gz',
    'train-labels-idx1-ubyte.gz',
    't10k-images-idx3-ubyte.gz',
    't10k-labels-idx1-ubyte.gz'
]

# 다운로드
if not os.path.exists(savepath):
    os.makedirs(savepath)
for f in files:
    url = baseurl + '/' + f
    loc = savepath + '/' + f
    if DEBUG:
        print("download: ", url)
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)

# gzip 압축해제
for f in files:
    gz_file = savepath + '/' + f
    raw_file = gz_file.replace('.gz', '')
    if DEBUG:
        print('gzip: ', f)
    with gzip.open(gz_file, 'rb') as fp:
        body = fp.read()
        with open(raw_file, 'wb') as w:
            w.write(body)

print('ok')
