# Reflection

## Planning out ideas
Originally, I wanted to create something that stored D&D characters and features so nothing would be missing when levelled up. The main issue I ran into with this was the sheer number of different features that would all have to be stored and fitted somewhere in order to keep track of everything. Between 13 classes and roughly 10 subclasses per class, and each of the 5 different features each one has is already too much, even if you only added the required detail for your character.

I still wanted to go with something creative, so in the end I went with something to store a character and organising which character fits into which events. I often have trouble when creating characters as they will be saved in several different places rather than one place. Most online services that lets you create a character and link them to events costs money, so I wanted to make my own low budget version of that.

## Comparing against each coding principle.

### Regular Expresions
I've used REGEX multiple times throughout my code to validate emails and dates. This ensures that input information is in the correct format and avoids potential crashes.
```python
if re.search(r"^\w+@\w+\.(ac\.uk|com)$", filename):
```
This one is checking for either a university email address (ending in ac.uk) or a generic email address like gmail (just ends in .com). Since this is also being used for the ``filename``, it also prevents users from putting an invalid filename when saving, possibly causing it to crash. This content is covered in week 7.

In addition, I have also used REGEX to create a valid date system in this ``DD-MM-YYYY....`` format.
```python
if re.search(r"^\d{2}-\d{2}-\d+$", start_date):
```
At the moment, this system doesn't allow for negative numbers, which is a change I will make in the future. This format also allows a working search system for dates and makes it easier to track when each one is relative to each other.

### Testing
While I haven't used unit testing (covered in week 7), I have implemented input validation for almost every single input in the program.
```python
def get_normal_input(prompt): #Makes sure the input isn't empty for important areas.
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please try again.")
```
The ``get_normal_input`` strips an input to check whether it is empty or not. This prevents errors when searching for something that doesn't have a name by forcing an input to have something in it.

In addition to ``get_normal_input``, I have not only used REGEX for input validation, but I have also used a try-catch to validate inputs.
```python
def modify_event(events, characters):
    try:
        event_id = int(input("Enter the ID of the event you want to modify: "))
    except:
        print("Invalid ID.")
        return
        ...
```
For example in ``modify_event``, this try-catch is being used to ensure that the ID is an integer and not anything else. Since ID's are only integers, this is to prevent trying to search something which would never have worked.

### Libraries
I have included multiple libraries such as:\
``re`` - Which has been used for regular expressions to validate emails and dates.\
``json`` - Which has been used to read and write to files, allowing for permanent storage of characters and events.
```python
with open(filename, "w") as file:
    json.dump(data, file, indent=4)
```
For example, being able to use the ``json`` library has let me reliably save and load my files. This is covered in week 6.

### File I/O
There is a clear features for reading and writing information to a file. Using the ``json`` library, I can reliably load any of the saves and rewrite old saves to keep my progress. This is covered in week 6.
```python
with open(filename, "w") as file:
    json.dump(data, file, indent=4)
```
```python
with open(filename, "r") as file:
    data = json.load(file)
```
Reading and writing to a file is what I found hardest when coding this assignment. It took me a long time to understand what exactly was being saved, and in what format. Not only that, it took me longer to understand that I had to recreate all the objects when loading them.

### Object-Oriented Programming
I've used both classes and inheritance in the program. The superclass ``StoryElement`` stores the base properties (``ID``, ``name``, ``description``) that both of its subclasses have. From there, the ``Character`` and ``Event`` subclasses add their specific attributes on top of it. This saves time having to rewrite similar functions for both subclasses. This is covered in week 8.

```python
def __init__(self, ID, name, description):
        self.ID = ID
        self.name = name
        self.description = description
```

As you can see below, using ``super().__init__``, I can reference the ``__init__`` function inside the superclass and call that when creating a character.

```python
def __init__(self, ID, name, description, species, role, abilities):
        super().__init__(ID, name, description)
        self.species = species
        self.role = role
        self.abilities = abilities
```
It also lets me have common functions used between the two, such as the ``display_basic_info(self)`` and ``update_name`` functions.

## Conclusion
Overall, despite how many different options there are to fill out and how long it took to make, I'm fairly happy with how this assignment has turned out, especially as my team project was extended to two days ago and I have had so little spare time for this. In the future, I would plan out the features of this earlier. I would also design it so that when a character ID is referenced by an event, it prints their name out as well as their ID. I would also take the time to properly lay out my code. Although I formatted it like this near the end, doing so from the start would have helped me stay organised.

It has been thanks to this course and this assignment that I have finally understood how classes and inheritance works. I have strengthened my skills in File I/O, as previously I've only ever needed to store one or two things, and this is a step up from that.
