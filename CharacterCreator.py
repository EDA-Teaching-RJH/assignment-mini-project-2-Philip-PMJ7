import re
import json

class StoryElement:
    '''StoryElement is a Superclass for both the Character and Event Subclasses.
    def __init__ is the setup for the Superclass.
    def display_basic_info is for displaying that information.
    Each of the remaining functions updates the names and descriptions respectively.'''
    def __init__(self, ID, name, description):
        self.id = ID
        self.name = name
        self.description = description

    def display_basic_info(self):
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")

    def update_name(self, new_name):
        self.name = new_name

    def update_description(self, new_description):
        self.description = new_description

class Event(StoryElement):
    '''Event is a subclass of StoryElement.
    Its purpose is to add events to this writing tool. It lets you add dates for searching as well as any character linked to said story event.
    def __init__ is for setting up the Subclass.
    def add_character will add the ID of a character to the event, and will display which characters are linked to the event.
    def remove_character will remove the ID of a character from the event.
    def update_time will ask for a new start/end date
    def display will display all the information of the event, from the name to the dates to the time.'''
    def __init__(self, ID, name, description, start_date, end_date, linked_characters):
        super().__init__(ID, name, description)
        self.start_date = start_date
        self.end_date = end_date
        if linked_characters: #If empty, it will be false. If it has anything, it will be true.
            self.linked_characters = linked_characters
        else:
            self.linked_characters = []

    
    def add_character(self, character_ID):
        if character_ID not in self.linked_characters: #If the ID passed in is not in the links list, it will be added.
            self.linked_characters.append(character_ID)


    def remove_character(self, character_ID): #Same as add_character but checks if the ID is there and then removes it.
        if character_ID in self.linked_characters:
            self.linked_characters.remove(character_ID)

    def display(self): #A variable called Character Names will be passed in here purely so that the linked characters print names and not just the ID's.
        super().display_basic_info()
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Linked Characters: {self.linked_characters}")

class Character(StoryElement):
    '''Character is a Subclass of StoryElement.
    Its purpose is to add a character to this writing tool. It lets you add more information for a character, like their role in the story, their species (non_humans?) and skills/powers.
    def __init__ is for setting up the Subclass.
    def update_species will update what species the character is.
    def update_role will update what role they are.
    def update_abilities updates their abilities.
    def display lists all of a character's information.'''
    def __init__(self, ID, name, description, species, role, abilities):
        super().__init__(ID, name, description)
        self.species = species
        self.role = role
        self.abilities = abilities

    def update_species(self, new_species):
        self.species = new_species
    
    def update_role(self, new_role):
        self.role = new_role
    
    def update_abilities(self, new_abilities): #This may be replaced by a tuple, which can give each ability an individual description.
        self.abilities = new_abilities #That will also let each ability be modular, adding and subtracting each one individually.
    
    def display(self):
        super().display_basic_info()
        print(f"Species: {self.species}")
        print(f"Role: {self.role}")
        print(f"Abilities: {self.abilities}")

def get_new_ID(current_IDs): #Starting at 1, it looks for the next available ID
    current = 1
    while current in current_IDs:
        current += 1
    return current

def create_character(current_IDs): #Menu Option 1
    ID = get_new_ID(current_IDs) #Obtains the next available ID
    name = input("Enter the character's name: ")
    species = input("Enter the character's species (e.g Human, Changeling, Dragonborn): ")
    description = input("Describe the character: ")
    role = input("What role (Mentor, Antagonist) do they play in the story?: ")
    abilities = input("Enter the character's abilities (Skills/Powers): ")

    character = Character(ID, name, description, species, role, abilities) #Creates an object of class Character

    return character

#UPDATE BOTH CREATES TO NOT ALLOW NULL INPUTS

def create_event(current_IDs): #Menu Option 2
    ID = get_new_ID(current_IDs)
    name = input("Enter the name of the Event: ")
    description = input("Describe the Event: ")
    while True:
        start_date = input("Enter the date the Event starts [DD-MM-(Any number of Y's)]: ")
        if re.search(r"^\d{2}-\d{2}-\d+$", start_date): #Checks for 2 numbers, followed by a dash, another 2 numbers, another dash, and any amount of numbers after that.
            break
        elif re.search(r"^\d{5,}$", start_date): #As long as there is 5 numbers minimum, it will try and turn that into a date.
            start_date = f"{start_date[:2]}-{start_date[2:4]}-{start_date[4:]}"
            YN = input (f"Did you mean to input {start_date} [Y/N]?: ")
            if YN.upper() == "Y":
                break
            elif YN.upper() == "N":
                print("Understood re-enter the date.")
            else:
                print("Please re-enter the date.")
        else:
            print("Does not fit the format. Try again.")
    
    while True: #Performs the same as start_date
        end_date = input("Enter the date the Event starts [DD-MM-(Any number of Y's)]: ")
        if re.search(r"^\d{2}-\d{2}-\d+$", end_date):
            break
        elif re.search(r"^\d{5,}$", end_date):
            end_date = f"{end_date[:2]}-{end_date[2:4]}-{end_date[4:]}"
            YN = input (f"Did you mean to input {end_date} [Y/N]?: ")
            if YN.upper() == "Y":
                break
            elif YN.upper() == "N":
                print("Invalid date, try again.")
            else:
                print("Please re-enter the date.")
        else:
            print("Does not fit the format. Try again.")
    
    print("The event will now be created. To link characters, navigate to Event Links through the menu.")

    linked_characters = []

    event = Event(ID, name, description, start_date, end_date, linked_characters) #Creates an object of class Event

    return event
    

def manage_links(event, characters): #Menu Option 3
    checked_ID = input("Please enter the ID of the ")

def search_all(characters, events): #Menu Option 5
    print("\n1. Search by Name")
    print("2. Search by Role (Characters)")
    print("3. Search by Date (Events)")

    choice = input("Choose search type: ")

    if choice == "1":
        name = input("Enter name: ").lower()

        print("\nCharacters Found:")
        for char in characters:
            if name in char.name.lower():
                char.display() #Searches all characters

                # Show linked events
                print("Appears in events:") #References which events each character is connected to.
                for event in events:
                    if char.id in event.linked_characters:
                        print(f"- {event.name}")

        print("\nEvents Found:") #Also just any event that fits the search
        for event in events:
            if name in event.name.lower():
                event.display()

    elif choice == "2":
        role = input("Enter role: ").lower()

        for char in characters: #Just which character fits their respective role.
            if role in char.role.lower():
                char.display()

    elif choice == "3":
        while True:
            date = input("Enter date [DD-MM-(Any number of Y's)]: ")
            if re.search(r"^\d{2}-\d{2}-\d+$", date):
                break
            elif re.search(r"^\d{5,}$", date):
                end_date = f"{date[:2]}-{date[2:4]}-{date[4:]}"
                YN = input (f"Did you mean to input {date} [Y/N]?: ")
                if YN.upper() == "Y":
                    break
                elif YN.upper() == "N":
                    print("Invalid date, try again.")
                else:
                   print("Please re-enter the date.")
            else:
                print("Does not fit the format. Try again.")

        for event in events:
            if date == event.start_date or date == event.end_date:
                event.display()

    else:
        print("Invalid option.")

def save_file(filename, characters, events): #Menu Option 6
    data = {
        "characters": [],
        "events": []
    }

    for char in characters: #Converts every Character object into a dictionary for JSON.
        data["characters"].append({
            "id": char.id,
            "name": char.name,
            "description": char.description,
            "role": char.role,
            "species": char.species,
            "abilities": char.abilities
        })
    
    for event in events: #Converts every Event object into a dictionary for JSON.
        data["events"].append({
            "id": event.id,
            "name": event.name,
            "description": event.description,
            "start_date": event.start_date,
            "end_date": event.end_date,
            "linked_characters": event.linked_characters
        })
    
    with open(filename, "w") as file: #Opens the file called filename and then writes into it.
        json.dump(data, file, indent = 4) #Writes a Python object to a file as JSON

    print("Data saved.")

def load_file(filename): #Menu Option 7
    try: #To prevent a crash if no file can be found.
        with open(filename, "r") as file:
            data = json.load(file)
    except:
        print("Error loading file.")
        return [], []

    characters = [] #Empties the previous character list to make space for the new ones.
    events = [] #Same as with characters, it empties the events list.

    for char_data in data["characters"]: #For each dictionary in the list of dictionaries.
        char = Character( #Takes each element in the dictionary and recreates an object of the character class.
            char_data["id"],
            char_data["name"],
            char_data["description"],
            char_data["role"],
            char_data["species"],
            char_data["abilities"]
        )
        characters.append(char)
    
    for event_data in data["events"]: #For each dictionary in the list of dictionaries.
        event = Event( #Takes each element in the dictionary and recreates an object of the character class.
            event_data["id"],
            event_data["name"],
            event_data["description"],
            event_data["start_date"],
            event_data["end_date"],
            event_data["linked_characters"]
        )
        events.append(event)
    
    print("Data Loaded.")
    return characters, events

def main():
    while True:
        filename = input ("Your files are stored under your email. Please enter your email to access the right file.")
        if re.search(r"^\w+@\w.+\.(ac.uk | com)$"):
            break
        else:
            print("That wasn't a valid email. Try again.")

    
    characters, events = load_file(filename)
    if characters == []:
        print("Nothing could be found under that email.")
        print("If this is your first time, you can save at any point to create your file. ")
        print("If you ever want to load a file, you can select that option from the menu.")
        print("--------------------------------------------------------")

    while True:
        print("\n--- MENU ---")
        print("1. Create Character")
        print("2. Create Event")
        print("3. Manage Links")
        print("4. View Characters and Events")
        print("5. Search All")
        print("6. Save")
        print("7. Load")
        print("8. Exit")

        choice = input("Please enter an option: ")

        if choice == "1": #Character Creation
            existing_ids = [char.id for char in characters]
            char = create_character(existing_ids)
            characters.append(char)
        
        elif choice == "2": #Event Creation
            existing_ids = [event.id for event in events]
            event = create_event(existing_ids)
            events.append(event)
        
        elif choice == "3": #Add or Remove Links
            asdasd
        
        elif choice == "4": #Displays all characters and event
            for char in characters:
                char.display()
            for event in events:
                event.display()
        
        elif choice == "5": #Full searching Feature
            search_all(characters, events)
        
        elif choice == "6": #Saves everything
            save_file(filename, characters, events)
        
        elif choice == "7": #Similar to earlier, it Loads a save.
            while True:
                filename = input("Please re-insert your email to access the file: [Type N to exit if accidental.]")
                if re.search(r"^\w+@\w.+\.(ac\.uk|com)$"):
                    characters, events = load_file(filename)
                    if characters == []:
                        print("Nothing under that email was found. Try again.")
                    else:
                        break
                elif filename.upper() == "N":
                    break
                else:
                    print("That wasn't a valid email. Try again.")

        elif choice == "8": #Exits out of the program.
            while True:
                pre_exit_choice = input("Make sure you'ved saved before you exit! Would you like to go back? [Y/N]:")
                if pre_exit_choice.upper() == "Y":
                    print("Exiting...") 
                    break
                elif pre_exit_choice.upper() == "N":
                    print("Returning to menu.")
                    break
                else:
                    print("Answer unclear. Looping.")

            if pre_exit_choice.upper() == "Y":
                break

main()