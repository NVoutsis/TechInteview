#Task_2
#2_1
import math
#Διάβασμα αρχείου .csv
file = open('class_2020_GIS.csv')

#2_2
lines = file.read().splitlines()
names = []
scores = []
newScores = []
listOfDictionaries = []

#Παράληψη επικεφαλίδων για τη μετατροπή της στήλης "scores" 
for i in range(1, len(lines)):
    names.append(lines[i].split(';')[0])
    scores.append(lines[i].split(';')[1])

#Μετατροπή κλίμακας από 1-10, σε 1-5
for score in scores:
    newScores.append(math.ceil(int(score) / 2))

#Δημιουργία Dictionary
for i in range(0,len(names)):
    my_dict = {'score': newScores[i], 'name': names[i]}
    listOfDictionaries.append(my_dict)

for dict in listOfDictionaries:
    print(dict)
