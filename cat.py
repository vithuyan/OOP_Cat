# Create a class called Cat
# Every cat should have three attributes when they're created: name, preferred_food and meal_time
# Create two instances of the Cat class in your file
# They should each have unique names, preferred foods and meal times
# Let's assume meal_time is an integer from 0 to 23 (representing the hour of the day in 24 hour time)
# Define a __str__() instance method.
# Add an instance method called eats_at that returns the hour of the day with AM or PM that this cat eats.
# The return value should be something like "11 AM" or "3 PM"
# Make sure your method returns this string rather than printing it
# Add another instance method called meow that returns a string of the cat telling you all about itself
# The return value should be something like "My name is Sparkles and I eat tuna at 11 AM"
# Call the meow method on each of the cats you instantiated in step 3

class Cat:


 def __intit__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time

def __str__(self,):
     return "Cat: name: {} - preferred_food: {} - meal_time: {}.". format(self.name, self.preferred_food, self.meal_time)

def eats_at(self):
    if self.meal_time < 12:
        return "{}AM.". format (self.meal_time)
    if self.meal_time == 12:
        return "{}PM.". format (self.meal_time)
    else:
        return "{}PM.". format (self.meal_time % 12)

def meow(self):
    return ("The cat's name is {} and his favourite food is {} and he eats at {}.". format (self.name, self.preferred_food, self.meal_time))


dobby = Cat("Dobby", "a big fish", 5)

harry = Cat("Harry", "dry meat", 5)

print (dobby.meow())                  
