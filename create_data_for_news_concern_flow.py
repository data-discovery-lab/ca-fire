import csv


# with open('data/topwords_news.csv') as filePointer:
#     csv_reader = csv.reader(filePointer, delimiter=',')
#     day = 7
#     concerns = []
#     day_concerns = dict()
#
#     for index, line in enumerate(csv_reader):
#
#         if index % 20 == 0:
#             day = day + 1
#             day_string = str(day)
#             if day < 10:
#                 day_string = '0' + day_string
#
#             day_key = '2018_11_' + day_string
#             day_concerns[day_key] = []
#             concerns = day_concerns[day_key]
#
#         concerns.append((line[0], line[1]))
#
#     print(day_concerns)



concern_data = {
    '2018_11_08': [('fire', '61'), ('paradise', '22'), ('acres', '14'), ('camp', '14'), ('thursday', '14'), ('county', '13'), ('air', '12'), ('butte', '12'), ('california', '12'), ('burned', '11'), ('town', '10'), ('burning', '9'), ('conditions', '9'), ('friday', '9'), ('mph', '9'), ('smoke', '9'), ('vehicles', '9'), ('weather', '9'), ('winds', '9'), ('evacuated', '8')],
    '2018_11_09': [('fire', '50'), ('california', '22'), ('angeles', '15'), ('los', '15'), ('flames', '14'), ('oaks', '14'), ('thousand', '13'), ('fires', '12'), ('homes', '12'), ('winds', '12'), ('shooting', '11'), ('burned', '10'), ('county', '10'), ('camp', '9'), ('friday', '9'), ('paradise', '9'), ('santa', '9'), ('burning', '8'), ('evacuated', '8'), ('firefighters', '8')],
    '2018_11_10': [('fire', '33'), ('california', '16'), ('malibu', '14'), ('county', '9'), ('burning', '8'), ('home', '8'), ('homes', '8'), ('wildfires', '8'), ('burned', '7'), ('fultz', '7'), ('officials', '7'), ('blaze', '6'), ('firefighters', '6'), ('fires', '6'), ('found', '6'), ('paradise', '6'), ('saturday', '6'), ('southern', '6'), ('wildfire', '6'), ('winds', '6')],
    '2018_11_11': [('california', '87'), ('fire', '73'), ('sunday', '31'), ('northern', '30'), ('wildfire', '29'), ('paradise', '27'), ('county', '23'), ('southern', '23'), ('homes', '22'), ('fires', '20'), ('malibu', '18'), ('burned', '17'), ('square', '17'), ('thursday', '17'), ('authorities', '16'), ('destroyed', '16'), ('home', '16'), ('officials', '16'), ('firefighters', '15'), ('house', '15')],
    '2018_11_12': [('fire', '80'), ('california', '38'), ('paradise', '31'), ('camp', '21'), ('fires', '19'), ('acres', '14'), ('county', '14'), ('town', '14'), ('winds', '14'), ('burned', '13'), ('firefighters', '13'), ('sunday', '13'), ('woolsey', '13'), ('homes', '11'), ('residents', '11'), ('contained', '10'), ('home', '10'), ('officials', '10'), ('wildfires', '10'), ('climate', '9')],
    '2018_11_13': [('fire', '59'), ('paradise', '17'), ('county', '16'), ('california', '14'), ('tuesday', '14'), ('authorities', '12'), ('firefighters', '11'), ('homes', '11'), ('remains', '11'), ('chief', '10'), ('woolsey', '10'), ('camp', '9'), ('wednesday', '9'), ('angeles', '8'), ('burned', '8'), ('los', '8'), ('wildfire', '8'), ('acres', '7'), ('fires', '7'), ('history', '7')],
    '2018_11_14': [('fire', '48'), ('california', '21'), ('county', '14'), ('camp', '13'), ('tuesday', '13'), ('contained', '10'), ('destroyed', '10'), ('acres', '9'), ('burned', '9'), ('butte', '9'), ('firefighters', '9'), ('officials', '9'), ('percent', '9'), ('wildfires', '9'), ('blaze', '8'), ('homes', '8'), ('structures', '8'), ('found', '7'), ('home', '7'), ('night', '7')],
    '2018_11_15': [('fire', '49'), ('california', '38'), ('wildfire', '21'), ('wildfires', '21'), ('evacuation', '20'), ('paradise', '15'), ('fires', '14'), ('blaze', '12'), ('smoke', '12'), ('town', '11'), ('authorities', '10'), ('residents', '10'), ('angeles', '9'), ('homes', '9'), ('los', '9'), ('plan', '9'), ('camp', '8'), ('flames', '8'), ('winds', '8'), ('burning', '7')],
    '2018_11_16': [('fire', '39'), ('california', '26'), ('paradise', '15'), ('rain', '14'), ('wildfire', '14'), ('destroyed', '13'), ('wednesday', '13'), ('acres', '10'), ('blaze', '10'), ('county', '10'), ('contained', '9'), ('homes', '9'), ('firefighters', '8'), ('found', '8'), ('remains', '8'), ('burned', '7'), ('butte', '7'), ('camp', '7'), ('missing', '7'), ('officials', '7')],
    '2018_11_17': [('fire', '78'), ('california', '25'), ('paradise', '23'), ('camp', '20'), ('ojai', '20'), ('nov', '18'), ('trump', '16'), ('president', '15'), ('thomas', '15'), ('wildfire', '13'), ('burned', '11'), ('homes', '11'), ('times', '11'), ('destroyed', '10'), ('officials', '10'), ('wildfires', '9'), ('chico', '8'), ('fires', '8'), ('history', '8'), ('home', '8')],
    '2018_11_18': [('fire', '67'), ('california', '45'), ('paradise', '36'), ('search', '36'), ('photo', '34'), ('nov', '33'), ('calif', '30'), ('file', '30'), ('camp', '25'), ('trump', '25'), ('northern', '24'), ('sunday', '24'), ('remains', '22'), ('wildfire', '20'), ('zone', '17'), ('chico', '16'), ('dozens', '16'), ('saturday', '16'), ('county', '15'), ('burned', '14')],
    '2018_11_19': [('fire', '29'), ('california', '12'), ('authorities', '8'), ('camp', '8'), ('burned', '6'), ('contained', '6'), ('nov', '6'), ('debris', '5'), ('destroyed', '5'), ('monday', '5'), ('paradise', '5'), ('burning', '4'), ('firefighters', '4'), ('percent', '4'), ('rain', '4'), ('victims', '4'), ('woolsey', '4'), ('acres', '3'), ('angeles', '3'), ('ash', '3')],
    '2018_11_20': [('fire', '54'), ('california', '28'), ('camp', '28'), ('rain', '24'), ('county', '16'), ('cbs', '14'), ('wildfires', '14'), ('butte', '12'), ('search', '12'), ('reports', '11'), ('expected', '10'), ('remains', '10'), ('residents', '10'), ('told', '10'), ('air', '9'), ('news', '9'), ('northern', '9'), ('paradise', '9'), ('lot', '8'), ('power', '8')],
    '2018_11_21': [('fire', '25'), ('california', '24'), ('rain', '24'), ('wednesday', '20'), ('firefighters', '13'), ('northern', '13'), ('wildfire', '12'), ('camp', '9'), ('francisco', '9'), ('nov', '9'), ('photo', '9'), ('san', '9'), ('deadly', '8'), ('killed', '8'), ('wildfires', '8'), ('flash', '7'), ('remains', '7'), ('risk', '7'), ('schwarzenegger', '7'), ('sheppard', '7')]
}


ignore_words = ['county', 'butte', 'update', 'everyone', 'socalfiresjameswoods', 'payitforward', 'visit', 'aaron',
                'buttestrong', 'chico', 'via', 'ohio', 'toll'
                ]
unique_words = set()

day_words_freq = dict()
for day, pair in concern_data.items():
    # print('data for day:', day)
    if day not in day_words_freq:
        day_words_freq[day] = dict()

    words_freq = day_words_freq[day]
    for w, freq in pair:
        if w in ignore_words:
            continue
        if int(freq) < 20:
            continue

        unique_words.add(w)
        words_freq[w] = int(freq)

print("days: ", concern_data.keys())
for c in unique_words:
    frequency_by_day = []
    for day in concern_data.keys():
        words_freq = day_words_freq[day]
        value = 0
        if c in words_freq:
            value = words_freq[c]

        frequency_by_day.append(value)

    print('{label: "' + str(c) + '", data:', frequency_by_day, '},')


print('unique words size:', len(unique_words))