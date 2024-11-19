
# импортируем вещи, читаем из файлика, делаем файлики (в csv)
import pandas as pd
wordies = pd.read_csv("/Users/anyamelnikova/Desktop/vs/untitled folder/Krasnoyarsk_aom2003-project.csv")
from pymystem3 import Mystem

import csv


    
with open('/Users/anyamelnikova/Desktop/vs/untitled folder/lemmas.csv', 'w', newline='') as csvfile:
    lem = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
def lemmas(wordies):
    with open('/Users/anyamelnikova/Desktop/vs/untitled folder/lemmas.csv', 'w', newline='') as csvfile:
        lem = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(wordies)):
            word = wordies['wordie'][i]
            m = Mystem()
            lemma = m.lemmatize(word)
            lemma = lemma[0]
            lem.writerow(['lemma@aom2003f', wordies['speaker'][i], wordies['time1'][i], wordies['time11'][i], wordies['time2'][i], wordies['time21'][i], wordies['duration'][i], wordies['duration1'][i]] + [lemma])


def morphs(wordies):
    with open('/Users/anyamelnikova/Desktop/vs/untitled folder/morph.csv', 'w', newline='') as csvfile:
        lem = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(wordies)):
            word = wordies['wordie'][i]
            m = Mystem()
            morphol = m.analyze(word)
            morphol =morphol [0]
            print(morphol)

            if 'analysis' in morphol:
                try:     
                    morph = str(morphol['analysis'][0]['gr'])
                except IndexError:
                    morph = str(morphol['text'])
            else:
                morph = str(morphol['text'])
               
            lem.writerow(['morph@aom2003f', wordies['speaker'][i], wordies['time1'][i], wordies['time11'][i], wordies['time2'][i], wordies['time21'][i], wordies['duration'][i], wordies['duration1'][i]] + [morph])
morphs(wordies)
lemmas(wordies)