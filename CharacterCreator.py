import re
import json

class StoryElement:
    '''StoryElement is a Superclass for both the Character and Event Subclasses.
    def __init__ is the setup for the superclass
    def display_basic_info is for displaying that information
    Each of the remaining functions updates the names and descriptions respectively'''
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_basic_info(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")

    def update_name(self, new_name):
        self.name = new_name

    def update_description(self, new_description):
        self.description = new_description