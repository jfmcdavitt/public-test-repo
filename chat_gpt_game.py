import random

def introduction():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious land filled with wonders.")
    print("Your goal is to explore and survive!")
    print()

def choose_location():
    locations = ["Forest", "Cave", "Castle"]
    print("Choose your location:")
    for index, location in enumerate(locations):
        print(f"{index + 1}: {location}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return locations[choice]

def encounter(location):
    encounters = {
        "Forest": ["a wild bear", "a friendly elf", "a hidden treasure"],
        "Cave": ["a lurking monster", "an ancient artifact", "a trap"],
        "Castle": ["a sleeping dragon", "a wise wizard", "a secret passage"],
    }
    return random.choice(encounters[location])

def play_game():
    introduction()
    while True:
        location = choose_location()
        result = encounter(location)
        print(f"You entered the {location} and encountered {result}!")
        
        if input("Do you want to explore again? (yes/no): ").lower() != "yes":
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
