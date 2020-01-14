def calc_bmi(h, w):
    bmi = w / (h/100) ** 2
    if bmi < 18.5:
        return 'thin'
    if bmi < 25:
        return 'normal'
    return 'fat'


if __name__ == "__main__":
    import random
    import os

    bmi_data_root = './bmi_data'
    bmi_csv = 'bmi.csv'
    bmi_csv_path = os.path.join(bmi_data_root, bmi_csv)

    if not os.path.exists(bmi_data_root):
        os.mkdir(bmi_data_root)
        print('mkdir')

    fp = open(bmi_csv_path, 'w', encoding='utf-8')
    fp.write('height,weight,label\r\n')

    cnt = {"thin": 0, "normal": 0, "fat": 0}
    for i in range(20000):
        h = random.randint(120, 200)
        w = random.randint(35, 80)
        label = calc_bmi(h, w)
        cnt[label] += 1
        fp.write("{},{},{}\r\n".format(h, w, label))
    fp.close()
    print("ok", cnt)
