from urllib.request import urlretrieve
import os

def get_dataset_file(url, savepath):
    if not os.path.exists(savepath):
        os.mkdir(os.path.dirname(savepath))
    urlretrieve(url, savepath)

if __name__ == "__main__":
    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    savepath = "wine_dataset/winequality-white.csv"

    get_dataset_file(url, savepath)
    