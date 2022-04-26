from models import *
import random
name_arr = ["Mustafa","Dad","Mom","Scam Likely","Eric","Kevin","Law","Luffy","Usopp","MEE6"]
db.drop_tables([People])
db.create_tables([People])

for i in range(10):
    People(name=name_arr[i], phone_number=(random.randint(1234567,99999999))).save()