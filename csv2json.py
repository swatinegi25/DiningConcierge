import csv

file1 = open("restaurantsearch.json", "w")  # append mode
id = 0
s = ""

with open("./results.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:

        #print(row[3])
        s += '{"index": {"_index": "restaurant", "_id": ' + str(id) + '}}\n'
        s += '{"business_id": "' + str(row[0]) + '", "cuisine": "' + row[3] + '"}\n'
        id += 1

    

file1.write(s)
file1.close()