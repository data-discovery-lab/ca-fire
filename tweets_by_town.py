import json
import pandas as pd
import csv


pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)

geojson_path = 'data/california-counties.geojson'
regionName = ['Alameda', 'Alpine', 'Amador', 'Butte', 'Calaveras', 'Colusa', 'Contra Costa', 'Del Norte', 'Tuolumne', 'El Dorado', 'Fresno', 'Glenn', 'Humboldt', 'Inyo', 'Lake', 'San Diego', 'San Francisco', 'Sierra', 'Siskiyou', 'Solano', 'Sonoma', 'Los Angeles', 'Madera', 'Marin', 'Mariposa', 'Mendocino', 'Merced', 'Modoc', 'Tulare', 'Imperial', 'Santa Cruz', 'Shasta', 'Stanislaus', 'Sutter', 'Tehama', 'Trinity', 'Kern', 'San Mateo', 'Santa Barbara', 'Santa Clara', 'Ventura', 'Yolo', 'Yuba', 'Lassen', 'Kings', 'Mono', 'Monterey', 'Napa', 'Nevada', 'Orange', 'Placer', 'Plumas', 'Riverside', 'Sacramento', 'San Benito', 'San Bernardino', 'San Joaquin', 'San Luis Obispo']


# read geojson to get coordinates
def read_polygon_json():
    multipolygon = []
    with open(geojson_path, encoding='utf-8') as geo_reader:
        json_data = geo_reader.read()
        d = json.loads(json_data)
        length = len(d["features"])
        for region in range(length):
            coordinates = d["features"][region]["geometry"]['coordinates']
            type = d["features"][region]["geometry"]['type']
            if type == 'Polygon':
                multipolygon.append([coordinates])
            else:
                multipolygon.append(coordinates)

    return multipolygon

#  isPointInPath: check ont point in one ploygon
def isPointInPath(x, y, poly):
    '''
    x, y -- x and y coordinates of point
    x: Longitude
    y: Latitude
    poly -- a list of tuples [(x, y), (x, y), ...]
    '''
    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if ((poly[i][1] > y) != (poly[j][1] > y)) and \
                (x < poly[i][0] + (poly[j][0] - poly[i][0]) * (y - poly[i][1]) /
                                  (poly[j][1] - poly[i][1])):
            c = not c
            break
        j = i
    return c  # return true/false means (lat, lon) is in/not in this polygon

# check one point in Multipolygon
def get_polygon_name_for_gps(x, y, multipolygon):
    for index in range(len(multipolygon)):

        poly_paths = multipolygon[index]
        for path in poly_paths:

            try:
                flag = isPointInPath(float(x), float(y), path[0])
                if flag:
                    return regionName[index]  # return region name
                else:
                    continue
            except:
                print('bad path at index', index, '; path:', path)
    return "unknown"



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


multipolygon = read_polygon_json()

#
# polygon_name = get_polygon_name_for_gps(29.9689, -95.6969, multipolygon=multipolygon)
# print("polygon name:", polygon_name)

# days = create_days()
days = ['2018_11_07']

for filename in days:
    with open('data/polygon_sentiment/polygon_sens_' + filename + '.csv', 'w') as sens_writer:
        csv_writer = csv.writer(sens_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        row = ['Tweet_id', 'Date', 'Hour', 'Minute', 'City', 'Location', 'Tweet', 'Afinn', 'Vader', 'SentiStrength', 'avg_sentiment', 'polygon']
        csv_writer.writerow(row)

        with open('data/raw_fire_sentiment/sens_' + filename + '.csv') as filePointer:
            csv_reader = csv.reader(filePointer, delimiter=',')
            for index, row in enumerate(csv_reader):
                if index < 1:
                    continue

                afinn = float(row[7])
                vader = float(row[8])
                senti = float(row[9])

                gps = row[5]
                gps = gps.split(',')

                lat = float(gps[0].strip())
                lon = float(gps[1].strip())
                polygon = get_polygon_name_for_gps(lat, lon, multipolygon=multipolygon)

                avg_sentiment = (afinn + 5*vader + 5*senti / 4) / 3
                row_data = row + [avg_sentiment, polygon]

                csv_writer.writerow(row_data)
