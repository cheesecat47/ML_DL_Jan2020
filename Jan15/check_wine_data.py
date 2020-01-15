import pandas as pd
import matplotlib.pyplot as plt

import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from get_dataset import get_dataset_file


if __name__ == "__main__":
    # 파일 있는지 확인
    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    savepath = "wine_dataset/winequality-white.csv"
    get_dataset_file(url, savepath)

    # 데이터 읽기
    wine = pd.read_csv(savepath, sep=';', encoding='utf-8')

    # 품질 데이터별로 그룹을 나누고 수 세어보기
    count_data = wine.groupby('quality')['quality'].count()

    # 수를 그래프로 그리기
    count_data.plot()
    plt.savefig('wine_dataset/wine_count_plt.png')
    plt.show()
    
