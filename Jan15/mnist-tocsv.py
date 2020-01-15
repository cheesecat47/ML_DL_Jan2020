import struct


def to_csv(name, maxdata):
    # 레이블 파일과 이미지 파일 열기
    lbl_f = open('./mnist/'+name+'-labels-idx1-ubyte', 'rb')
    img_f = open('./mnist/'+name+'-images-idx3-ubyte', 'rb')
    csv_f = open('./mnist/'+name+'.csv', 'w', encoding='utf-8')

    # 헤더 정보 읽기 - 바이너리를 원래대로 변환.
    mag, lbl_count = struct.unpack('>II', lbl_f.read(8)) # 매직코드 + 레이블 개수
    mag, img_count = struct.unpack('>II', img_f.read(8)) # 매직코드 + 이미지 개수
    rows, cols = struct.unpack('>II', img_f.read(8))
    pixels = rows * cols
    print('IMG size: {} * {} = {}'.format(rows, cols, pixels))

    # 이미지 데이터를 읽고 csv로 저장하기
    res = []
    for idx in range(lbl_count):
        if idx > maxdata:
            break
        label = struct.unpack('B', lbl_f.read(1))[0] # 무슨 숫자인지
        bdata = img_f.read(pixels) # 28 * 28 읽어와서
        sdata = list(map(lambda n: str(n), bdata)) # 문자열로 변환
        csv_f.write(str(label)+',') # 제일 앞에 레이블 쓰고
        csv_f.write(','.join(sdata)+'\r\n') # 그 다음 픽셀 데이터 쓰고 줄바꿈

        # 잘 저장됐는지 이미지 파일로 저장해서 테스트하기
        if idx < 10:
            s = 'P2 28 28 255\n'
            s += ' '.join(sdata)
            iname = './mnist/{}-{}-{}.pgm'.format(name, idx, label)
            with open(iname, 'w', encoding='utf-8') as f:
                f.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()


if __name__ == "__main__":
    # 결과를 파일로 출력하기
    to_csv('train', 1000)
    to_csv('t10k', 500)
