import os

import csv
import codecs
import json
import sqlite3


def export_json(fn, data):
    savename = './{}.json'.format(fn)
    jdata = json.dumps(data)
    with open(savename, mode='w', encoding='utf-8') as fo:
        fo.write(jdata)


def export_csv(fn, data):
    savename = './{}.csv'.format(fn)
    with codecs.open(savename, mode='w', encoding='utf-8') as fo:
        writer = csv.writer(fo, delimiter=',', quotechar='"')
        writer.writerows(data)


if __name__ == "__main__":
    filepath = 'test2.sqlite'

    if not os.path.isfile(filepath):
        print("no file")
        exit(0)

    conn = sqlite3.connect(filepath)
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM items"
    )
    fr_list = cur.fetchall()
    for fr in fr_list:
        print(fr)

    filename = filepath.split()[0]
    export_json(filename, fr_list)
    export_csv(filename, fr_list)

