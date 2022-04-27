#
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

# Create your views here.
options = ["get_cardname", "get_price", "get_stats"]

cards = []

class TaskForm(forms.Form):
    card_name = forms.CharField(label="Card Name")

import requests as r

def get_raw_data_by_name(card)-> bool:
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
            

def get_price(name):
    """_summary_
    Args:
        name (_type_, optional): _description_. Defaults to None.
    Returns:
        int: _description_
    """
    #currency = specify_currency()
    if validate_name(name):
        res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
        json_response = res.json()
        return f"""The cost of {name} is {json_response["prices"]['usd']}"""
    else:
        return "Sorry, that was not a valid name"

     

# def price(request,name):
#     return render(request, "backpack:price", {
#         "name": get_raw_data_by_name(name),
#         "price": get_price(get_raw_data_by_name(name))
#     })

# def form(request):
#      if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             card_name = form.cleaned_data["card_name"]
  
#         args = {"form": form, "card_name": card_name}
#         return render(request, "backpack/forms.html", args)


def make_hello():
    return "Function output goes here"

def func():
    return "Sample function output here"

def index(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            card_name = form.cleaned_data["card_name"]  
    
            args = {
                    "options": options,
                    "hello": make_hello,
                    "recent_searches": cards,
                    "form": form,
                    "card_name": get_raw_data_by_name(card_name),
                    "card_price": get_price(card_name)             
                    }
            return render(request, "backpack/index.html", args)
        else:
            return HttpResponse("FAILED ATTEMPT")
    else:
        return HttpResponse("FAILED ATTEMPT")



def library(request):
    return HttpResponse("This page will be the library.")

#create functions here that CRUD the library

# def greet(request, name):
#     return render(request, "backpack/greet.html", {
#         "name": name.lower()
#     })


    
# def add(request):    
#     return render(request, "backpack/add.html", {
#         "func": func                  
#      })


#create functions here that SEARCH apis