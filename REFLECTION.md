# Reflection

## Planning out ideas
Originally, I wanted to create something that stored D&D characters and and features so nothing would be missing when levelled up. The main issue I ran into with this was the sheer number of different features that would all have to be stored and fitted somewhere in order to keep track of everything. Between 13 classes and roughly 10 subclasses per class, and each of the 5 different features each one has is already too much, even if you only added the required detail for your character.

I still wanted to go with something creative, so in the end I went with something to store a character and organising which character fits into which events.

## Comparing against each coding principle.

### Regular Expresions
I've used REGEX multiple times throughout my code, mainly for checking specific inputs like the date or the email used for the filename.

### Testing
While I haven't used unit testing, I have implemented input validation for almost every single input.

### Libraries
I have included multiple libraries, such as re for the regular expressions and json in order to read/write to files.

### File I/O
There is a clear features for reading and writing information to a file.

### Object-Oriented Programming
I've used both classes and inheritence in the program. The superclass StoryElement stores the base properties (ID, name, description) that both of it subclasses have. From there, the Character and Event subclasses add their specific attributes on top of it.