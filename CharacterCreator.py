import re
import json

# ==========================================
# CLASSES AND SUPERCLASSES
# ==========================================

class StoryElement:
    '''StoryElement is a Superclass for both the Character and Event Subclasses.
    def __init__ is the setup for the Superclass.
    def display_basic_info is for displaying that information.
    Each of the remaining functions updates the names and descriptions respectively.'''
    def __init__(self, ID, name, description):
        self.ID = ID
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
    
    def update_abilities(self, new_abilities):
        self.abilities = new_abilities
    
    def display(self):
        super().display_basic_info()
        print(f"Species: {self.species}")
        print(f"Role: {self.role}")
        print(f"Abilities: {self.abilities}")

# ==========================================
# SET UP
# ==========================================

def get_new_ID(current_IDs): #Starting at 1, it looks for the next available ID
    current = 1
    while current in current_IDs:
        current += 1
    return current

def get_normal_input(prompt): #Makes sure the input isn't empty for important areas.
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please try again.")

# ==========================================
# CHARACTERS
# ==========================================

def create_character(current_IDs): #Menu Option 1
    ID = get_new_ID(current_IDs) #Obtains the next available ID
    name = get_normal_input("Enter the character's name: ")
    species = get_normal_input("Enter the character's species (e.g Human, Changeling, Dragonborn): ")
    description = get_normal_input("Describe the character: ")
    role = get_normal_input("What role (Mentor, Antagonist) do they play in the story?: ")
    abilities = get_normal_input("Enter the character's abilities (Skills/Powers): ")

    character = Character(ID, name, description, species, role, abilities) #Creates an object of class Character

    return character

def modify_character(characters):
    try:
        char_ID = int(input("Enter the ID of the character you want to modify: "))
    except:
        print("Invalid ID.")
        return

    selected_char = None
    for char in characters:
        if char.ID == char_ID:
            selected_char = char
            break

    if selected_char is None:
        print("Character not found.")
        return

    while True:
        print(f"\nModifying {selected_char.name} (ID {selected_char.ID})")
        print("1. Name")
        print("2. Description")
        print("3. Species")
        print("4. Role")
        print("5. Abilities")
        print("6. Exit")

        choice = input("Which attribute would you like to update? ")

        if choice == "1": #Input Validation (kind of) for each one of these.
            selected_char.update_name(get_normal_input("Enter new name: "))
        elif choice == "2":
            selected_char.update_description(get_normal_input("Enter new description: "))
        elif choice == "3":
            selected_char.update_species(get_normal_input("Enter new species: "))
        elif choice == "4":
            selected_char.update_role(get_normal_input("Enter new role: "))
        elif choice == "5":
            selected_char.update_abilities(get_normal_input("Enter new abilities: "))
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

# ==========================================
# EVENTS
# ==========================================

def create_event(current_IDs): #Menu Option 2
    ID = get_new_ID(current_IDs)
    name = get_normal_input("Enter the name of the Event: ")
    description = get_normal_input("Describe the Event: ")
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
    
def modify_event(events, characters):
    try:
        event_id = int(input("Enter the ID of the event you want to modify: "))
    except:
        print("Invalid ID.")
        return

    selected_event = None
    for event in events:
        if event.ID == event_id:
            selected_event = event
            break

    if selected_event is None:
        print("Event not found.")
        return

    while True:
        print(f"\nModifying {selected_event.name} (ID {selected_event.ID})")
        print("1. Name")
        print("2. Description")
        print("3. Start Date")
        print("4. End Date")
        print("5. Exit")

        choice = input("Which attribute would you like to update? ")

        if choice == "1":
            selected_event.update_name(get_normal_input("Enter new name: "))
        elif choice == "2":
            selected_event.update_description(get_normal_input("Enter new description: "))
        elif choice == "3":
            selected_event.start_date = get_normal_input("Enter new start date [DD-MM-YYYY]: ")
        elif choice == "4":
            selected_event.end_date = get_normal_input("Enter new end date [DD-MM-YYYY]: ")
        elif choice == "5":
            break
        else:
            print("Invalid choice.") #manage_links Handles the modifying of links instead of modify event.

def manage_links(events, characters): #Menu Option 3
    try:
        event_ID = int(input("Enter the Event ID you want to manage: "))
    except:
        print("Invalid ID.")
        return

    #Finds the event
    selected_event = None
    for event in events:
        if event.ID == event_ID:
            selected_event = event
            break

    if selected_event is None:
        print("Event not found.")
        return
    
    while True:
        print("\n1. Add Character Link")
        print("2. Remove Character Link")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try: #Input Validation
                char_ID = int(input("Enter Character ID to add: "))
            except:
                print("Invalid ID.")
                continue

            for char in characters:
                if char.ID == char_ID:
                    selected_event.add_character(char_ID)
                    print(f"{char.name} linked.")
                    break
            else:
                print("Character not found.")

        elif choice == "2":
            try:
                char_ID = int(input("Enter Character ID to remove: "))
            except:
                print("Invalid ID.")
                continue

            selected_event.remove_character(char_ID)
            print("Link removed (if it existed).")

        elif choice == "3":
            break

        else:
            print("Invalid option.")

# ==========================================
# SEARCHING
# ==========================================

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
                    if char.ID in event.linked_characters:
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
        while True: #Same system as the date checks.
            date = input("Enter date [DD-MM-(Any number of Y's)]: ")
            if re.search(r"^\d{2}-\d{2}-\d+$", date):
                break
            elif re.search(r"^\d{5,}$", date):
                date = f"{date[:2]}-{date[2:4]}-{date[4:]}"
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

# ==========================================
# SAVING AND LOADING
# ==========================================

def save_file(filename, characters, events): #Menu Option 6
    data = {
        "characters": [],
        "events": []
    }

    for char in characters: #Converts every Character object into a dictionary for JSON.
        data["characters"].append({
            "ID": char.ID,
            "name": char.name,
            "description": char.description,
            "role": char.role,
            "species": char.species,
            "abilities": char.abilities
        })
    
    for event in events: #Converts every Event object into a dictionary for JSON.
        data["events"].append({
            "ID": event.ID,
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
            char_data["ID"],
            char_data["name"],
            char_data["description"],
            char_data["role"],
            char_data["species"],
            char_data["abilities"]
        )
        characters.append(char)
    
    for event_data in data["events"]: #For each dictionary in the list of dictionaries.
        event = Event( #Takes each element in the dictionary and recreates an object of the character class.
            event_data["ID"],
            event_data["name"],
            event_data["description"],
            event_data["start_date"],
            event_data["end_date"],
            event_data["linked_characters"]
        )
        events.append(event)
    
    print("Data Loaded.")
    return characters, events

# ==========================================
# MAIN LOOP
# ==========================================

def main():
    while True:
        filename = input ("Your files are stored under your email. Please enter your email to access the right file.")
        if re.search(r"^\w+@\w+\.(ac\.uk|com)$", filename):
            break
        else:
            print("That wasn't a valid email. Try again.")

    
    characters, events = load_file(filename) #Tries to load immediately, even though you can manually later. It makes things easier.
    if characters == []:
        print("Nothing could be found under that email.")
        print("If this is your first time, you can save at any point to create your file. ")
        print("If you ever want to load a file, you can select that option from the menu.")
        print("--------------------------------------------------------")

    while True:
        print("\n--- MENU ---")
        print("1. Create Character")
        print("2. Modify Character")
        print("3. Create Event")
        print("4. Modify Event")
        print("5. Manage Links")
        print("6. View Characters and Events")
        print("7. Search All")
        print("8. Save")
        print("9. Load")
        print("10. Exit")

        choice = input("Please enter an option: ")

        if choice == "1": #Character Creation
            existing_IDs = [char.ID for char in characters]
            char = create_character(existing_IDs)
            characters.append(char)
        
        elif choice == "2": #Modifies Character Traits
            modify_character(characters)
        
        elif choice == "3": #Event Creation
            existing_IDs = [event.ID for event in events]
            event = create_event(existing_IDs)
            events.append(event)
        
        elif choice == "4": #Modifies Event Traits
            modify_event(events, characters)

        elif choice == "5": #Add or Remove Links
            manage_links(events, characters)
        
        elif choice == "6": #Displays all characters and event
            for char in characters:
                char.display()
            for event in events:
                event.display()
        
        elif choice == "7": #Full searching Feature
            search_all(characters, events)
        
        elif choice == "8": #Saves everything
            save_file(filename, characters, events)
        
        elif choice == "9": #Similar to earlier, it Loads a save.
            while True:
                filename = input("Please re-insert your email to access the file: [Type N to exit if accidental.]")
                if re.search(r"^\w+@\w+\.(ac\.uk|com)$", filename):
                    characters, events = load_file(filename)
                    if characters == []:
                        print("Nothing under that email was found. Try again.")
                    else:
                        break
                elif filename.upper() == "N":
                    break
                else:
                    print("That wasn't a valid email. Try again.")

        elif choice == "10": #Exits out of the program.
            while True:
                pre_exit_choice = input("Make sure you have saved before you exit! Would you like to go back? [Y/N]:")
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