import requests as r

def get_card_by_name(name=None)-> str:
    """Gets the name of a card and searches for it
       on scryfall.net. If no name is provided, ask the
       user in the fucntion call. If the card does not 
       exist, ask the user if they would like to re enter
       another card name before quitting.

    Args:
        name (str): The name of the card to be searched
        for. Defaults to None.

    Returns:
        str: The card if found, else None.
    """
    if name:
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        if res.status_code == 404:
            replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
            if 'y' in replay:
                get_card_by_name(name)
            else:
               return "Goodbye" 
        else:
            print(res.text)
    else:            
        name = input("Enter a card name: ")
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        if res.status_code == 404:
            replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
            if 'y' in replay:
                get_card_by_name()
            else:
               return "Goodbye"
        else:
            print(res.text)    
    return res.text

    
get_card_by_name("The wandering emperor")
get_card_by_name()


def get_card_price(name=None)->int:
    """_summary_

    Args:
        name (_type_, optional): _description_. Defaults to None.

    Returns:
        int: _description_
    """
    pass

def get_playable_stats(name=None)-> int:
    """_summary_

    Args:
        name (_type_, optional): _description_. Defaults to None.

    Returns:
        int: _description_
    """
    pass


   
#how to print a price
#print(res.json()['prices'])

#returns entire kamigawa set
# kamigawa = r.get("https://api.scryfall.com/cards/search?order=set&q=e:neo")

# print(kamigawa)

# #retrieve one random card from set = kaimgawa
# random_card = r.get("https://api.scryfall.com/cards/random?q=e:neo")