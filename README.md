# Game of Thrones Houses Dictionary

This project contains a Python dictionary that provides information 
about the main houses in the Game of Thrones series and their 
associated characters. Each house dictionary includes details 
about the main characters such as their name, position, and partner.

## How to Use

To access the information in the dictionary, you can use the 
provided function `show_characters()`. This function accepts 
keyword arguments corresponding to the houses you want to display. 
If no arguments are provided, it will display characters from all 
houses.

Example:

```python
# Import the dictionary and the function
from game_of_thrones_houses import game_of_thrones_houses, show_characters

# Display characters from House Stark and House Lannister
show_characters(House_Stark=game_of_thrones_houses["House Stark"], House_Lannister=game_of_thrones_houses["House Lannister"])
