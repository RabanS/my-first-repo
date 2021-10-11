file = open("hola.txt")

for line in file:
    print(line)

file.close()
 

band = ["Jonny", "Joe", "Marky", "Dee-Dee"]

# file=open("ramones.txt", "w")

with open("ramones2.txt", "w") as file:
    for member in band:
        file.write(member + "\n"  )

#%%
import csv

with open("records.csv") as file:
    reader = csv.DictReader(file)
    doctors = 0
    for row in reader:
        if row ["profession"] == "doctor":
            doctors = doctors +1


    print("there are " + str(doctors) + " doctors in the file")

#%%
beatles = [
    {"name": "John Lennon", "role": "singer"},
    {"name": "Paul McCartney", "role": "bass"},
    {"name": "George Harrison", "role": "guitar"},
    {"name": "Ringo Starr", "role": "drums"},
]
with open("beatles.csv", "w") as file:
    column_names = ["name", "role"]

    writer = csv.DictWriter(file, column_names)
    writer.writeheader()
    for beatle in beatles:
        writer.writerow(beatle)

with open("beatles.csv") as file:
    reader =  csv.DictReader(file)
    for row in reader:
        print(row)