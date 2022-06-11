import requests as r

def get_raw_data_by_name(name=None)-> bool:
    """Gets the raw data of a card and searches for it
       on scryfall.net. If no name is provided, ask the
       user in the fucntion call. If the card does not 
       exist, ask the user if they would like to re enter
       another card name before quitting.
    Args:
        name (str): The name of the card to be searched
        for. Defaults to None.
    Returns:
        bool: True if the card was found, Flase otherwise.
    """
    if name:
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        if res.status_code >= 404:
            replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
            if 'y' in replay:
                get_raw_data_by_name(name)
            else:
                return False          
        else:
            print(res.text)
            return True
    else:            
        name = input("Enter a card name: ")
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        if res.status_code >= 404:
            replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
            if 'y' in replay:
                get_raw_data_by_name()
            else:
                return False          
        else:
            print(res.text)
            return True    
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
    if currency.strip().lower() not in results:
        return
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
        if res.status_code >= 404:
            replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
            if 'y' in replay.lower().strip():
                get_card_price(name)
            else:
               return "Goodbye" 
        else:
            json_response = res.json()
            price = json_response["prices"][currency]
            print(price)
            return price
    else:
        name = input("Enter a card name: ")
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        if res.status_code >= 404:
            replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
            if 'y' in replay.lower().strip():
                get_card_price()
            else:
                return "Goodbye"
        else:
            json_response = res.json()
            price = json_response["prices"][currency]
            print(price)
            return price          


#get_card_price("Tamiyo's Safekeeping")

def get_playable_stats(name=None)-> int:
    """_summary_
    Args:
        name (_type_, optional): _description_. Defaults to None.
    Returns:
        int: _description_
    """
    pass

def get_set_names():
    """_summary_

    Returns:
        _type_: _description_
    """
    pass

def get_set():
    pass





   
#how to print a price
#print(res.json()['prices'])

#returns entire kamigawa set
# kamigawa = r.get("https://api.scryfall.com/cards/search?order=set&q=e:neo")

# print(kamigawa)

# #retrieve one random card from set = kaimgawa

###!!!parse just the name out and add to libarary later

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
        if self.validate_name(name) == False:
            return False
        else:
            if name not in self.data:
                self.data[name] = 1
                self.size += 1
            else:
                self.data[name] += 1
                self.size += 1
        return True
            
    
    def validate_name(self, name:str)->bool:
        """Check to make sure the card name 
        is found in the api call.

        Args:
            name (str): Card name to be searched.

        Returns:
            bool: True if the card was found, False otherwise.
        """
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        if res.status_code >= 404:
           return False
        else:
            return True
            
    def show_library(self)->bool:
        """Show all cards and their amounts.

        Returns:
             True
        """
        print(self.data)
        return True
    
    def remove(self, name:str)->bool:
        """Removes a card from the library.

        Args:
            name (str): Card name to be removed.

        Returns:
            bool: True if removal was success,
                  False if not successful.
        """
        if self.is_empty():
            print(self.data)
            return False
        else:
            if self.validate_name(name):
                self.data.pop(name)                               
                self.size -= 1
                return True
            else:
                print("Sorry that card is not in the library.")
                return False
    
    def clear(self)->bool:
        """Remove all cards from the library.

        Returns:
            bool: True if successful,
                  False if not successful.
        """
        self.data.clear()
        self.size = 0
        return self.size == 0
    
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
    
    def get_random_capp(self)->str:
        """Makes an api call to get a random
        card from the Streets of new Cappena set.

        Returns:
            str: Name of a random card from the SNC set.
        """
        random_card = r.get("https://api.scryfall.com/cards/random?q=e:snc")
        return random_card.json()['name']
    
    
    def get_random_kami(self)->str:
        """Makes an api call to get a random
        card from the KAMIGAWA NEO set.

        Returns:
            str: Name of a random card from the Neo set.
        """
        random_card = r.get("https://api.scryfall.com/cards/random?q=e:neo")
        return random_card.json()['name']
    
    def get_name(self)->str:
        """Gets the name of a card from the database

        Returns:
            str: name of card.
        """
        if self.is_empty():
            print("Empty Library")
            return False
        else:
            options = [name for name in self.data.keys()]
            print(options)
            card = str(input("Type the card you wish to get:"))
            if self.validate_name(card):
                return card
            else:
                print("That is not a valid name, Goodbye!")
                return False
                    
        
    def __str__(self)->str:
        sb = ""
        if self.is_empty():
            return "There is nothing in your library."
        else:
            for k,v in self.data.items():
                builder = f'Name: {k} Count: {v}'
                sb += builder
            return sb


