import matplotlib.pyplot as plt
from matplot_font import set_font
import numpy as np

KIND = int(input('>>'))

if KIND == 1:
    plt.title = '라인 플로트'
    plt.plot(['a', 'c', 'e'], [3, 5, 7])
    plt.plot(['a', 'b', 'c', 'd'], [1, 2, 3, 4])
    plt.xlabel = 'x'

if KIND == 2:
    y = [5, 3, 7, 10, 9, 5, 3.5, 8]
    x = range(len(y))
    plt.bar(x, y, width=0.7, color='blue')
    plt.show()
    plt.savefig('test.png')

elif KIND == 3:
    plt.rc('font', family=set_font())
    plt.rcParams['axes.unicode_minus'] = False

    plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c='b', lw=6,
             ls='--', marker='p', ms=15, mec='g', mew=5, mfc='r')
    plt.title('스타일 적용 예')
    plt.xlim(0, 50)
    plt.ylim(-10, 30)
    plt.show()

elif KIND==4:
    names=['groupA','groupB','groupC']
    values=[1,10,100]

    plt.figure()

    plt.subplot(131) # 행, 열, 번호
    plt.bar(names, values)

    plt.subplot(132) # 행, 열, 번호
    plt.scatter(names, values)

    plt.subplot(133) # 행, 열, 번호
    plt.bar(names, values)

    plt.show()

