import random
import time
import datetime

location = 'Clermont'
district = 'District 07'
revision = "stuff"
user = input("what's your name? ")
currentTime = time.asctime()
date = datetime.datetime.now()

print(f"{'Location: ' + location:<25} Revision: {revision}")
print(f"{'District: ' + district:<25} Date: {date}")
print(f"{'User: ' + user:<25} Time: {currentTime}")

print(f"{date:%B %d, %Y}")