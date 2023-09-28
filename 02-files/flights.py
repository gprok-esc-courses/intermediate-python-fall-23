# Use flights.csv from Kaggle

flights_file = open('flights.csv')

lines = flights_file.readlines()

carriers = []
counter = 0     # Used to avoid adding the label of the first (0) row
for line in lines:
    tokens = line.split(',')
    if counter > 0 and tokens[10] not in carriers:
        carriers.append(tokens[10])
    counter += 1

print(carriers)
