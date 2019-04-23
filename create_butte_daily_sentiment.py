import csv
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

def create_days():
    d = '2018_11_'
    result = []
    for i in range(7, 23):
        md = str(i)

        if i < 10:
            md = '0' + str(i)

        my_day = d + md
        result.append(my_day)

    return result

folder = 'data/butte_sentiment'

days = create_days()


start_date = 7

NUM_DAYS = 16
NUM_HOURS = 24
butte_data = np.zeros( (NUM_DAYS, NUM_HOURS))

for day in days:

    filepath = folder + '/sens_' + day + '.csv'
    with open(filepath) as filePointer:
        csv_reader = csv.reader(filePointer, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index < 1:
                continue

            afinn = float(row[7])
            vader = float(row[8])
            senti = float(row[9])

            avg_sentiment = (afinn + 5 * vader + 5 * senti / 4) / 3

            date = row[1]
            date_no = int(date.split('-')[2])
            date_index = date_no - start_date
            hour = int(row[2])

            converted_senti = (avg_sentiment*(-1) + 5)
            butte_data[date_index][hour] = butte_data[date_index][hour] + converted_senti



ax = sns.heatmap(butte_data, linewidth=0.1,  cmap="PiYG")
plt.show()
