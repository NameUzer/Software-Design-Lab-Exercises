from random import randint

class Die(object):
   ''' this class represents a six sided die.'''
   def __init__(self):
       ''' Sets the initial face of the die.'''
       self.value = 1

   def roll(self):
       """Resets the die's value to a random number
         between 1 and 6."""
       self.value = randint(1, 6)

   def getvalue(self):
       """Returns the current face of the die."""

       return self.value

   def __str__(self):
       """Returns the string rep of the die."""

       return str(self.value)

