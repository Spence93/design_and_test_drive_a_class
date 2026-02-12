# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicHistory():
  

    def __init__(self):
        # Parameters:
        
        # Side effects:
        #   Create empty list to store tracks
        
    def add_track(self, song)
        #Parameters: song = string

        #Side effect - add song to track list


    def get_tracks(self)
        #return:    
        #       List of tracks added    
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
When class initialised, check empty list is created
"""
history = MusicHistory()
expected = []


"""
given a valid string, the track is added to the list
"""
history = MusicHistory()
history.add_track("song1")
expected = ["song1"]

"""
Given a non string, check that correct exception raised
"""
history = MusicHistory()
history.add_track(5)
expected = TypeError "error string" 

"""
given a valid string, the track is added to the list
with multiple calls
"""
history = MusicHistory()
history.add_track("song1")
history.add_track("song2")
history.add_track("song3")
expected = ["song1", "song2", "song3"]


"""
Check that correct list is displayed to user
"""
istory = MusicHistory()
history.add_track("song1")
history.add_track("song2")
history.add_track("song3")
actual = get_tracks()
expected = ["song1", "song2", "song3"]



_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
