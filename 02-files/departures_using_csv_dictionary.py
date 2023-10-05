import csv

flights_file = open('flights.csv')

dict_reader = csv.DictReader(flights_file, delimiter=',')

for row in dict_reader:
    print(row['id'], row['carrier'])

