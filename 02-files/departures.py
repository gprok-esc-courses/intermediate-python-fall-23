# Use flights.csv from Kaggle

flights_file = open('flights.csv')

lines = flights_file.readlines()

origins = {}
counter = 0     # Used to avoid adding the label of the first (0) row
for line in lines:
    tokens = line.split(',')
    if counter > 0:
        origin = tokens[13]
        if origin in origins:
            origins[origin] += 1
        else:
            origins[origin] = 1
    counter += 1

print(origins)


