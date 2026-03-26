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
        self.date = start_date
        if linked_characters: #If empty, it will be false. If it has anything, it will be true.
            self.linked_characters = linked_characters
        else:
            self.linked_characters = []

    
    def add_character(self, character_ID):
        if character_ID not in self.linked_characters:
            self.linked_characters.append(character_ID)


    def remove_character(self, character_ID):
        if character_ID in self.linked_characters:
            self.linked_characters.remove(character_ID)

    def display(self): #A variable called Character Names will be passed in here purely so that the linked characters print names and not just the ID's.
        super().display_basic_info
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
        super().display_basic_info
        print(f"Species: {self.species}")
        print(f"Role: {self.role}")
        print(f"Abilities: {self.abilities}")
