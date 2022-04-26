from models import *
from playhouse.shortcuts import model_to_dict, dict_to_model

game_over = False
print("\n\nEnter just 'q' at any input to exit input \n\n")
while not game_over:
    mode = input("'c' to enter CREATION mode or any other key to (not 'q') view all contacts : ")
    if mode == "q":
        game_over=True
    elif mode == "c":   
        print("\n Creation mode \n")
        name = input("Enter Name : ")
        if name != 'q':
            number = input("Enter Phone number : ")
            if number != 'q':
                new_contact = dict_to_model(People,{"name":name,"phone_number":number})
                new_contact.save()
                print("\n Success 👍 \n")
        print("\n Leaving CREATION MODE \n")
    else:   
        print("\n All contacts \n")
        for person in People.select():
            print(model_to_dict(person),"\n")
        print("\n")

        
  