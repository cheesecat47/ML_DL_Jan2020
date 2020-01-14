def scatter(lbl, colour):
    # 서브 플롯 전용 - 지정한 레이블을 임의의 색으로 칠하기
    b = tbl.loc[lbl]
    ax.scatter(b['weight'], b['height'], c=colour, label=lbl)

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pandas as pd

    # pandas로 csv 읽기
    tbl = pd.read_csv('./bmi_data/bmi.csv', index_col=2)

    # 그래프 그리기 시작
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    scatter('fat', 'red')
    scatter('normal','yellow')
    scatter('thin','purple')

    ax.legend()
    plt.savefig('./bmi_data/bmi-test.png')
    plt.show()

