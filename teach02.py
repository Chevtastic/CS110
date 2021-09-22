
print("Please enter the following information:\n")

fName = input("First Name: ")
lName = input("Last Name: ")
email = input("Email Address: ")
phNum = input("Phone Number: ")

jobTitle = input("Job Title: ")
idNum = input("ID Number: ")

# Stretch details
hair = input("Hair Color: ")
eyes = input("Eye Color: ")
month = input("Start Month: ")
training = input("Training complete (Yes/No)?: ")

#print user ID Card
print(f"The ID Card is:")
print(f"----------------------------------------")
print(f"{lName.upper()}, {fName.capitalize()}")
print(f"{jobTitle.title()}")
print(f"ID: {idNum}\n")

print(f"{email.lower()}")
#print(f"{phNum}\n")

#Phone number formatting to add parenthesis and dash 
print(f"({phNum[:3]}) {phNum[3:7]}-{phNum[7:]}\n")

print(f"{'Hair: ' + hair.capitalize():<25} {'Eyes: ' + eyes.capitalize()}")
print(f"{'Month: ' + month.capitalize():<25} {'Training: ' + training.capitalize()}")
print(f"----------------------------------------")
