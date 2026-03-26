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
    def display will display all the information of the event, from the name to the dates to the time.'''
    def __init__(self, ID, name, description, start_date, end_date, linked_characters):
        super().__init__(ID, name, description)
        self.start_date = start_date
        self.end_date = end_date
        self.date = start_date
        self.linked_characters =