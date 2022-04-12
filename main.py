import requests as r

#things to do:
#raise bad json errors, stronger queries, add librarary oop syntax


class Library():
    
    def __init__(self, library={}):
        self.library = library
    
  


def get_raw_data_by_name(name=None)-> str:
    """Gets the raw data of a card and searches for it
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
                get_raw_data_by_name(name)
            else:
                return            
        else:
            print(res.text)
    else:            
        name = input("Enter a card name: ")
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        if res.status_code == 404:
            replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
            if 'y' in replay:
                get_raw_data_by_name()
            else:
                return           
        else:
            print(res.text)    
    return res.text

#get_raw_data_by_name()

#This function gets specified currency from user
def specify_currency()->str:
    """Asks the user for which currency they wish to use.

    Returns:
        str: Type of currency the user selects. None otherwise
    """
    results = ["usd", "usd_foil", "usd_etched", "eur", "eur_foil", "tix"]
    display_options = '''Select from one of the following currencies:\n"usd", "usd_foil", "usd_etched", "eur", "eur_foil", "tix"'''    
    print(display_options)
    currency = str(input("Enter currency: "))
    if currency.lower() not in results:
        return None
    else:
        return currency
    
#This function gets the card price 
def get_card_price(name=None)->int:
    """_summary_

    Args:
        name (_type_, optional): _description_. Defaults to None.

    Returns:
        int: _description_
    """
    currency = specify_currency()
    if name:
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        if res.status_code == 404:
            replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
            if 'y' in replay:
                get_card_price(name)
            else:
               return "Goodbye" 
        else:
            json_response = res.json()
            print(json_response["prices"][currency])
    else:
        name = input("Enter a card name: ")
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        if res.status_code == 404:
            replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
            if 'y' in replay:
                get_card_price()
            else:
                return "Goodbye"
        else:
            json_response = res.json()
            print(json_response["prices"][currency])          


get_card_price("Mox Opal")

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