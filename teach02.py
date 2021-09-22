

fName = input("First Name: ")
lName = input("Last Name: ")
email = input("Email Address: ")
phNum = input("Phone Number: ")

jobTitle = input("Job Title: ")
idNum = input("ID Number: ")
hair = input("Hair Color: ")
eyes = input("Eye Color: ")
month = input("Start Month: ")
training = input("Training complete? (Y/N): ")



print(f"The ID Card is:")
print(f"----------------------------------------")
print(f"{lName.upper()}, {fName.capitalize()}")
print(f"Job title: {jobTitle.title()}")
print(f"ID: {idNum}\n")

print(f"{email.lower()}")
print(f"{phNum}\n")
#print(f"({phNum[:3]}) {phNum[3:7]}-{phNum[7:]}")
print(f"----------------------------------------")
