import requests as r

#things to do:
#raise bad json errors, stronger queries, add librarary oop syntax
print(r)

class Library():
    
    def __init__(self):
        self.data = {}
        self.size = 0
    
    def add(self, name:str)->bool:
        """Add a card to the library.

        Args:
            name (str): card name to be added 

        Returns:
            bool: returns True if card is added,
                    False if the card was not 
                    found in the api call.
        """
        pass
    
    def show_library(self)->None:
        """Show all cards and their amounts.

        Returns:
             None
        """
        pass
    
    def remove(self, name:str)->bool:
        """Removes a card from the library.

        Args:
            name (str): Card name to be removed.

        Returns:
            bool: True if removal was success,
                  False if not successful.
        """
        pass
    
    def clear(self)->bool:
        """Remove all cards from the library.

        Returns:
            bool: True if successful,
                  False if not successful.
        """
        pass
    
    def get_size(self)->int:
        """Get the total numbert of 
        cards in the library.

        Returns:
            int: Total nuber of cards in libaray.
        """
        return self.size
    
    def is_empty(self)-> bool:
        """Check to see if there are 
        cards in the library.
        Returns:
            bool: True if empty, False otherwise.
        """
        return self.size == 0
        
    def __str__(self):
        if self.is_empty():
            return "There is nothing in your library."
        else:
            return "".join(str(x) for x in self.data)

#this tests an empty library
lib = Library()
print(lib)

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


#get_card_price("Mox Opal")

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