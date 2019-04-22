import csv
import subprocess
import shlex
import os.path
import sys

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer

from afinn import Afinn


#######################################################################################################
## Modify the three lines below to make this program work on your computer.                          ##
## Be careful with the direction of the slashes / and include a slash at the end of the second path. ##
#######################################################################################################
SentiStrengthLocation = "sentistrength/SentiStrength.jar" #This must point to the location of SentiStrength on your computer
SentiStrengthUnzippedTextFilesLocation = "sentistrength/SentiStrength_Data/" #This must point to the location of the unzipped SentiStrength data files on your computer

#Test file locations and quit if anything not found
if not os.path.isfile(SentiStrengthLocation):
    print("SentiStrength not found at: ", SentiStrengthLocation)
    sys.exit()

if not os.path.isdir(SentiStrengthUnzippedTextFilesLocation):
    print("SentiStrength data folder not found at: ", SentiStrengthUnzippedTextFilesLocation)
    sys.exit()



day = '2018_11_07'
folder = 'data/raw_fire'
def create_days():
    d = '2018_11_'
    result = []
    for i in range(8, 31):
        my_day = d + str(i)
        result.append(my_day)

    return result


# Just to test if SentiStrength it working
def senti_strength_rate_sentiment(sentiString):
    #open a subprocess using shlex to get the command line string into the correct args list format
    p = subprocess.Popen(shlex.split("java -jar '" + SentiStrengthLocation + "' stdin sentidata '" + SentiStrengthUnzippedTextFilesLocation + "' scale"), stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #communicate via stdin the string to be rated. Note that all spaces are replaced with +
    #Can't send string in Python 3, must send bytes
    b = bytes(sentiString.replace(" ","+"), 'utf-8')
    stdout_byte, stderr_text = p.communicate(b)
    #convert from byte
    stdout_text = stdout_byte.decode("utf-8")
    #remove the tab spacing between the positive and negative ratings. e.g. 1    -5 -> 1 -5
    stdout_text = stdout_text.rstrip().replace("\t"," ")
    points = stdout_text.split(' ')
    if len(points) < 1:
        return None
    try:
        return float(points[len(points)-1])
    except:
        return None


## VADER sentiment
analyzer = SentimentIntensityAnalyzer()
## AFINN sentiment
afinn = Afinn(emoticons=True)

days = [day]
# days = create_days()
for d in days:
    with open('data/raw_fire_sentiment/sens_' + d + '.csv', 'w') as sens_writer:
        csv_writer = csv.writer(sens_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        row = ['Tweet_id', 'Date', 'Hour', 'Minute', 'City', 'Location', 'Tweet', 'Afinn', 'Vader', 'SentiStrength']
        csv_writer.writerow(row)

        with open(folder + '/camfire_' + day + '.csv') as filePointer:
            csv_reader = csv.reader(filePointer, delimiter=',')
            for index, row in enumerate(csv_reader):
                if index < 1:
                    continue

                sentence = row[6]
                word_scores = afinn.scores(sentence)

                if len(word_scores) == 0:
                    print('cannot AFINN score sentence:', sentence)
                    continue

                afine_total_score = float(sum(word_scores))
                afine_avg_score = afine_total_score / len(word_scores)

                vd = analyzer.polarity_scores(sentence)
                if 'compound' not in vd:
                    print('cannot VADER score sentence:', sentence)
                    continue

                vd_compound = vd['compound']
                senti_score = senti_strength_rate_sentiment(sentence)

                if senti_score is None:
                    print('cannot SentiStrength score sentence:', sentence)
                    continue
                row_data = row + [afine_avg_score, float(vd_compound), float(senti_score)]

                csv_writer.writerow(row_data)



