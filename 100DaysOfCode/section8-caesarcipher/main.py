#simple funtion
def greet():
    print("Hi.")
    print("How is you today?")
    print("Ins't the weather nice today?")

greet()

#function that allows for input

def greet_with_name(name):
    print(f"Hi {name}")
    print(f"How are you today {name}?")
    print(f"{name} ins't the weather nice today?")    

greet_with_name("Weslley")

#function with more than 1 input

def greet_with(name, location):
    print(f"Hi {name}")
    print(f"How are you today {name}?")
    print(f"{name} ins't the weather nice today in {location}?")    

greet_with("Weslley", "Malta")