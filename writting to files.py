#Create a file called guests.txt and write the names of five guests to it.
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

# Now, replace the names of the guests with a new list of three guests.
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "w") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()


# Now, remove the names of two guests from the file.

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")



# Now, check if two guests are checked in or not.

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))