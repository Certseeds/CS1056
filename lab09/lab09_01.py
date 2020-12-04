import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    spindles = pd.read_csv("./", sep=";")
    pd.read_csv("./spindles.csv", sep=";")
    row_num, column_num = spindles.shape    
    time_series_freq = 0.005  # 5*10^-3, 200HZ
    temp = spindles['SS']
    print(spindles.head())
    features = ["EOG Left[uV]", "EEG C3-A1[uV]", "EEG O1-A1[uV]", "EEG C4-A1[uV]", "EEG O2-A1[uV]", "SS"]

    for x in features:
        spindles[x] = [x.replace(',', '.') for x in spindles[x]]
    for name_of_order in features:
        x = np.arange(0, row_num / 100, 0.01)
        y = spindles[name_of_order]
        y_array = []
        for i in y:
            y_array.append(float(i))
        y_array = pd.Series(y_array,dtype=float)
        print(y_array.min())
        print(y_array.max())
        print(y_array.mean())
        # print(y.groupby(features[0])[features[0]].min())
        plt.figure(num=3)
        plt.title(features[0])
        plt.ylim(-100, 100)

        plt.plot(x, y_array, alpha=0.6, label=name_of_order)
        plt.xlabel('row')
        plt.ylabel('column')

        plt.legend()
        plt.show()
        print("123")


if __name__ == '__main__':
    main()
