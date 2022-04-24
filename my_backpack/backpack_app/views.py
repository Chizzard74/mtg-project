from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
options = ["get_cardname", "get_price", "get_stats"]

import requests as r

def get_raw_data_by_name(card=None)-> bool:
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
    
    if validate_name(card):
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={card}")
        return res.json()['name']
    else:
        return "Sorry, That card is not a valid option."
        
def validate_name(name:str)->bool:
    """Check to make sure the card name 
    is found in the api call.

    Args:
        name (str): Card name to be searched.

    Returns:
        bool: True if the card was found, False otherwise.
    """
    res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
    if res.status_code >= 400:
        return False
    else:
        return True
            
    # else:            
    #     name = input("Enter a card name: ")
    #     res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
    #     if res.status_code >= 404:
    #         replay =  input("Sorry That is not a valid card name,\nDo you want to try again: type 'yes or no?'")
    #         if 'y' in replay:
    #             get_raw_data_by_name()
    #         else:
    #             return False          
    #     else:
    #         print(res.text)
    #         return True  
    
    return res.text

def forms(request):
    return render(request, "backpack/forms.html")

def make_hello():
    return "Function output goes here"

def func():
    return "Sample function output here"

def index(request):
    return render(request, "backpack/index.html", {
        "options": options,
        "hello": make_hello
    })

def library(request):
    return HttpResponse("This page will be the library.")

#create functions here that CRUD the library

def greet(request, name):
    return render(request, "backpack/greet.html", {
        "name": name.lower()
    })
    
def add(request, card):
    return render(request, "backpack/add.html", {
        "func": func,
        "card": card,
        "raw": get_raw_data_by_name(card)
    })


#create functions here that SEARCH apis