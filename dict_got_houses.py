"""
The dictionary game_of_thrones_houses contains information about the main houses
in Game of Thrones and their associated characters.
Each house dictionary includes details about the main characters.
In turn, the main characters are described by their name, occupation, and partner.
"""

game_of_thrones_houses = {
    "House Stark": {
        "Ned": {
            "Name": "Eddard Stark",
            "Position": "Lord of Winterfell / Hand of the King",
            "Partner": "Catelyn Stark"
        },
        "Catelyn": {
            "Name": "Catelyn Stark",
            "Position": "Lady of Winterfell",
            "Partner": "Eddard Stark"
        },
        "Robb": {
            "Name": "Robb Stark",
            "Position": "King in the North",
            "Partner": "Talisa Stark"
        },
        "Sansa": {
            "Name": "Sansa Stark",
            "Position": "Lady of Winterfell / Queen in the North",
            "Partner": "Tyrion Lannister (forced marriage), Ramsay Bolton"
        },
        "Arya": {
            "Name": "Arya Stark",
            "Position": "Assassin",
            "Partner": "Gendry"
        },
        "Bran": {
            "Name": "Bran Stark",
            "Position": "King of the Six Kingdoms",
            "Partner": "No partner"
        },
        "Jon": {
            "Name": "Jon Snow",
            "Occupation": "Lord Commander of the Night's Watch",
            "Partner": "Ygritte, Daenerys Targaryen"
        },
    },
    "House Lannister": {
        "Tywin": {
            "Name": "Tywin Lannister",
            "Position": "Hand of the King / Head of House Lannister",
            "Partner": "Joanna Lannister"
        },
        "Jaime": {
            "Name": "Jaime Lannister",
            "Position": "Kingsguard / Lord Commander",
            "Partner": "Cersei Lannister"
        },
        "Cersei": {
            "Name": "Cersei Lannister",
            "Position": "Queen Regent / Queen of the Seven Kingdoms",
            "Partner": "Robert Baratheon, Jaime Lannister, Euron Greyjoy"
        },
        "Tyrion": {
            "Name": "Tyrion Lannister",
            "Position": "Hand of the King / Hand of the Queen",
            "Partner": "Sansa Stark (forced marriage), Shae"
        }
    },
    "House Targaryen": {
        "Daenerys": {
            "Name": "Daenerys Targaryen",
            "Position": "Khaleesi of the Great Grass Sea / Breaker of Chains / Mother of Dragons",
            "Partner": "Khal Drogo, Hizdahr zo Loraq, Jon Snow"
        },
        "Viserys": {
            "Name": "Viserys Targaryen",
            "Position": "Exiled Prince",
            "Partner": "No partner"
        }
    }
}

def show_characters(**kwargs):
    for key_house, value_house in kwargs.items():
        for key_character, value_character in value_house.items():
            print(f"In {key_house} one of the main characters is: {key_character} ")
            print("Character details:")
            for key_character_details, value_character_details in value_character.items():
                print(f"{key_character_details} => {value_character_details}")
            print('\n---------')

show_characters(**game_of_thrones_houses)


