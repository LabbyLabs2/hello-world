import csv

data = []
with open('transposecsv.csv') as f:
    for row in csv.reader(f):
        data.append(row)
    print(data)

#find index of header, then get the same index position for each row
Trying to add text
Adding yet another comment
#I like cheese. There are many types of cheese in the world, some types are mild, others are strong and smelly. They can be used in cooking or are good on top of crackers as an appetizer. What is the best way to store cheese?
