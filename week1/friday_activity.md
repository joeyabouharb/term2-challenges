#### Build a Cat Class
​
Build a `Cat` class.
​
Each cat should have a name.
Implement a speak method to say meow.
Add each cat's name to the speak method (Pixie says meow).
​
```python
class Dog:
    def __init__(self, dog_name, dog_age):
        '''
        A _dunder_ method, which runs when a new object is instantiated from this class. When creating this object it must be passed a dog_name string and a dog_age int.
        '''
        this.dog_name = dog_name
        this.dog_age = dog_age
        print("I've been initialized!")
​
    def speak(self):
        '''
        Prints the dogs name and age.
        '''
        print(f'{this.dog_name} says woof! I am {this.dog_age} years old!')
​
​
doggo = Dog('Rover', 2)
doggo.speak()
​
doggo = Dog('Lassie', 5)
doggo.speak()
```
​
Using the above code as a starting point:
​
We've got name and age, let's give each dog a location too. Test your location works by printing the dog's location.
​
```python
⋮
doggo = Dog('Rover', 2, 'Brisbane')
doggo.location
Brisbane
```
​
Create a walk method. This should say "I have been for X walks.". Every time you call walk, the number should increase by one E.g:
`doggo = Dog(...)`
(To do this you are going to have to look into 'setters', have a google)
`doggo.walk()` # -> I have been for 1 walks today
`doggo.walk()` # -> I have been for 2 walks today
​
Update the walk method so it only increases the walk count. Create a new method to display walks. E.g.: `doggo = Dog(...)`
`doggo.walk()` # -> Shouldn't print anything on screen
`doggo.walk()` # -> Shouldn't print anything on screen
`doggo.display_walks()` # -> I have been for 2 walks today
Update the walk method so you can chain walk commands. E.g.: `doggo = Dog(...)`
`doggo.walk.walk.display_walks()` # -> I have been for 2 walks today
​
#### Classes: Beast Mode
​
Improve the `walk` method. Accept a location and a distance. e.g. `doggo.walk('Brisbane', 20)`
Update your `display_walks` method to show all of the walk details.
Implement a `total_distance` method to calculate the total distance of all the walks.
Track the time each walk is created. Update `display_walks` to show it back to your user in a readable format.
Use a pip package to geocode a location and store it's latitude + longitude. E.g. "Brisbane" stores -27.44888,153.00531