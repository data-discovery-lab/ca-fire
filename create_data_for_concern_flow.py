concern_data = {'2018_11_08': [('paradise', 82), ('fire', 79), ('smoke', 60), ('county', 55), ('butte', 53), ('evacuation', 39), ('update', 37), ('prayer', 37), ('please', 35)],
                '2018_11_09': [('fire', 148), ('smoke', 129), ('paradise', 105), ('everyone', 100), ('people', 89), ('help', 83), ('chico', 80), ('safe', 72), ('hillfire', 66), ('please', 62)],
                '2018_11_10': [('fire', 247), ('smoke', 112), ('people', 96), ('help', 92), ('socalfiresjameswoods', 82), ('please', 80), ('safe', 72), ('everyone', 70), ('affected', 69), ('history', 65)],
                '2018_11_11': [('help', 114), ('fire', 105), ('please', 76), ('firefighter', 71), ('paradise', 58), ('people', 51), ('via', 45), ('victim', 44), ('missing', 44), ('smoke', 43)],
                '2018_11_12': [('help', 155), ('affected', 113), ('fire', 104), ('home', 64), ('death', 58), ('toll', 50), ('people', 49), ('paradise', 49), ('deadliest', 45), ('via', 44)],
                '2018_11_13': [('fire', 72), ('help', 61), ('paradise', 49), ('please', 44), ('people', 38), ('death', 32), ('paradisefire', 32), ('animal', 30), ('via', 29), ('update', 28)],
                '2018_11_14': [('fire', 65), ('affected', 57), ('animal', 50), ('help', 49), ('paradise', 47), ('smoke', 38), ('people', 34), ('via', 30), ('firefighter', 30), ('missing', 29)],
                '2018_11_15': [('smoke', 70), ('fire', 62), ('air', 46), ('paradise', 36), ('help', 35), ('victim', 35), ('quality', 31), ('san', 30), ('chico', 29), ('missing', 28)],
                '2018_11_16': [('air', 56), ('help', 50), ('missing', 49), ('smoke', 48), ('fire', 44), ('please', 38), ('quality', 33), ('paradise', 33), ('people', 32), ('airquality', 27)],
                '2018_11_17': [('visit', 44), ('president', 44), ('help', 43), ('fire', 40), ('paradise', 36), ('people', 34), ('victim', 30), ('smoke', 28), ('please', 28), ('via', 24)],
                '2018_11_18': [('fire', 59), ('paradise', 33), ('help', 29), ('state', 22), ('started', 22), ('air', 22), ('via', 21), ('chico', 19), ('forest', 19), ('story', 19)],
                '2018_11_19': [('fire', 41), ('paradise', 23), ('via', 21), ('victim', 20), ('smoke', 18), ('update', 17), ('deadliest', 16), ('help', 16), ('thank', 14), ('people', 14)],
                '2018_11_20': [('smoke', 25), ('fire', 18), ('victim', 17), ('paradise', 17), ('ohio', 17), ('via', 16), ('god', 15), ('help', 14), ('county', 14), ('democrat', 13)],
                '2018_11_21': [('retweet4good', 123), ('buttestrong', 45), ('help', 45), ('rain', 39), ('victim', 27), ('aaron', 25), ('thank', 24), ('payitforward', 24), ('fire', 23), ('relief', 22)],
                #'2018_11_22': [('retweet4good', 25), ('help', 10), ('payitforward', 10), ('buttestrong', 10)],
                #'2018_11_23': [('help', 15)],
                #'2018_11_24': [('fire', 14)],
                #'2018_11_25': [('contained', 23), ('retweet4good', 13), ('help', 13), ('fire', 12), ('paradise', 10)],
                #'2018_11_26': [('112campfire', 24), ('fire', 12), ('loss', 10), ('grief', 10), ('resource', 10)],
                #'2018_11_27': [('help', 27), ('112campfire', 24), ('victim', 18), ('givingtuesday', 17), ('housing', 15), ('support', 14), ('affected', 12), ('helping', 10), ('resource', 10), ('paradise', 10)],
                # '2018_11_28': [('gender', 63), ('reveal', 59), ('video', 54), ('8million', 54), ('show', 53), ('fire', 13), ('112campfire', 10), ('help', 10)],
                # '2018_11_29': [('video', 68), ('new', 62), ('place', 62), ('story', 60), ('favorite', 60), ('112campfire', 14), ('paradise', 13), ('child', 10), ('disaster', 10), ('chanc', 10)],
                # '2018_11_30': [('113campfire', 23), ('help', 17), ('disaster', 11)]
                }


ignore_words = ['county', 'butte', 'update', 'everyone', 'socalfiresjameswoods', 'payitforward', 'visit', 'aaron',
                'buttestrong', 'chico', 'via', 'ohio', 'toll'
                ]
unique_words = set()

day_words_freq = dict()
for day, pair in concern_data.items():
    print('data for day:', day)
    if day not in day_words_freq:
        day_words_freq[day] = dict()

    words_freq = day_words_freq[day]
    for w, freq in pair:
        if w in ignore_words:
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