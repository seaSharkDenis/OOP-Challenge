from pet import Pet

name = input("Enter the name of your pet: ")
pet = Pet(name)
print(f"\nA new pet named {pet.name} has been created!\n")

while True:
    print("What would you like to do!")
    print("1. Feed your pet")
    print("2. Let your pet sleep")
    print("3. Play with your pet")
    print("4. Teach your pet a new trick")
    print("5. Show learned tricks")
    print("6. Check pet status")
    print("7. Exit\n")

    choice = input("Enter your choice (1-7): ")

    if(choice == "1"):
        pet.eat()
    elif(choice =="2"):
        pet.sleep()
    elif(choice =="3"):
        pet.play()
    elif(choice =="4"):
        trick = input("Enter the name of the trick: ")
        pet.train(trick)
    elif(choice =="5"):
        print(f"Tricks: {', '.join(pet.show_tricks())}")
    elif(choice =="6"):
        pet.get_status()
    elif(choice =="7"):
        print(f"Thanks for playing with {pet.name}! Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
