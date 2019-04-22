import json
import pandas as pd
import csv
import os

counties = ['Alameda', 'Alpine', 'Amador', 'Butte', 'Calaveras', 'Colusa', 'Contra Costa', 'Del Norte', 'Tuolumne', 'El Dorado', 'Fresno', 'Glenn', 'Humboldt', 'Inyo', 'Lake', 'San Diego', 'San Francisco', 'Sierra', 'Siskiyou', 'Solano', 'Sonoma', 'Los Angeles', 'Madera', 'Marin', 'Mariposa', 'Mendocino', 'Merced', 'Modoc', 'Tulare', 'Imperial', 'Santa Cruz', 'Shasta', 'Stanislaus', 'Sutter', 'Tehama', 'Trinity', 'Kern', 'San Mateo', 'Santa Barbara', 'Santa Clara', 'Ventura', 'Yolo', 'Yuba', 'Lassen', 'Kings', 'Mono', 'Monterey', 'Napa', 'Nevada', 'Orange', 'Placer', 'Plumas', 'Riverside', 'Sacramento', 'San Benito', 'San Bernardino', 'San Joaquin', 'San Luis Obispo']

folder = '/home/long/TTU-SOURCES/ca-fire/data/counties'

def extract_cities_for_county(county):

    standardized_county = '_'.join(county.lower().split())
    filepath = folder + '/' + standardized_county + '.txt'

    if not os.path.isfile(filepath):
        raise Exception('not found county data file', filepath)

    cities = [standardized_county]
    with open(filepath) as filePointer:
        for line in filePointer:
            city = '_'.join(line.lower().split())
            cities.append(city)

    return standardized_county, cities


def get_county_from_city(city, counties_cities):
    if counties is None:
        return 'unknown'

    standardized_city = '_'.join(city.lower().split())
    for county, cities in counties_cities.items():
        if standardized_city in cities:
            return county

    return 'unknown'


def create_days():
    d = '2018_11_'
    result = []
    for i in range(7, 31):
        md = str(i)
        if i < 10:
            md = '0' + str(i)
        my_day = d + str(md)
        result.append(my_day)

    return result


counties_cities = dict()
for c in counties:
    county, cities = extract_cities_for_county(c)
    counties_cities[county] = cities


days = create_days()
# days = ['2018_11_07']

for filename in days:
    with open('data/counties_sentiment/county_sens_' + filename + '.csv', 'w') as sens_writer:
        csv_writer = csv.writer(sens_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        row = ['Tweet_id', 'Date', 'Hour', 'Minute', 'City', 'Location', 'Tweet', 'Afinn', 'Vader', 'SentiStrength', 'avg_sentiment', 'county']
        csv_writer.writerow(row)

        with open('data/raw_fire_sentiment/sens_' + filename + '.csv') as filePointer:
            csv_reader = csv.reader(filePointer, delimiter=',')

            unknown_count = 0
            for index, row in enumerate(csv_reader):
                if index < 1:
                    continue

                afinn = float(row[7])
                vader = float(row[8])
                senti = float(row[9])

                city = row[4]
                county = get_county_from_city(city, counties_cities=counties_cities)

                if county == 'unknown':
                    unknown_count = unknown_count + 1
                    print("unknown city:", city, 'total:', unknown_count)

                avg_sentiment = (afinn + 5*vader + 5*senti / 4) / 3
                row_data = row + [avg_sentiment, county]

                csv_writer.writerow(row_data)
