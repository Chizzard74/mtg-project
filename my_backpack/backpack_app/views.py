from random import Random
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from backpack_app.models import *
import random
from django.contrib.auth import authenticate, login, logout



# Create your views here.

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
        #message =  f"""The cost of {json_response['name']} is {json_response["prices"]['usd']}."""
        return f"""{json_response['name']}: ${json_response["prices"]['usd']}"""
    else:
        return "Sorry, that was not a valid name"


# def form(request):
#      if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             card_name = form.cleaned_data["card_name"]
  
#         args = {"form": form, "card_name": card_name}
#         return render(request, "backpack/forms.html", args)

def process_form(form, session_data):
    if form.is_valid():
            name = form.cleaned_data["card_name"]
            res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
            json_response = res.json()
            img = json_response['image_uris']['normal']
            title = json_response['name']            
            args = {
                "name": name,
                "card_price": get_price(name),
                "img": img,
                'title': title,
                'session_data': session_data                                
            }
            return args
    return False



def index(request):
    print(request.session.items())

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("backpack:login_view"))
    return render(request, "backpack/index.html")

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("backpack:index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "backpack/login_view.html",)
    return render(request, "backpack/login_view.html")

def logout_view(request):
    logout(request)
    return render(request, "backpack/logout_view.html", {
                "message": "Logged Out"
            })

def price(request):
    if request.method == "POST":
        form = TaskForm(request.POST)            
        if form.is_valid():
            name = form.cleaned_data["card_name"]            
            res = r.get(f"https://api.scryfall.com/cards/named?fuzzy={name}")
            json_response = res.json()
            img = json_response['image_uris']['normal']
            title = json_response['name']
            try:
                request.session['name'] += [title]
                args = {
                "name": name,
                "card_price": get_price(name),
                "img": img,
                'title': title,
                'req': request.session['name']
                }
                print(request.session.items())
                return render(request, "backpack/resources.html", args)
            except:
                request.session['name'] = [title]
                args = {
                    "name": name,
                    "card_price": get_price(name),
                    "img": img,
                    'title': title,
                    'req': request.session['name']
                    }                         
                print(request.session.items())
                return render(request, "backpack/resources.html", args)               
    return render(request, 'backpack/price.html')

def card_view(request):
    return render(request, 'backpack/card_view.html')

def color(request):
    return render(request, 'backpack/color.html')

def resources(request):       
    return render(request, 'backpack/resources.html')

def add(request):
    session_name_data = request.session['name']    
    args = {
        "session_name_data": session_name_data            
    }
    return render(request, "backpack/add.html", args)

def library(request):
    try:
        name_dict = request.session['name']
        no_duplicates = set(name_dict)
        args={        
            "added_card": no_duplicates
        }  
        return render(request, 'backpack/library.html', args)
    except:
        request.session['name'] = []
        return render(request, 'backpack/library.html')
             
   
    #return HttpResponse("This page will be the library.")
    
def purchase(request, card=None):
    req = request.GET.get("buy")
    args ={
        "card": card,
        "req": req,
    }
    return render(request, "backpack/purchase.html", args)

def form_page(request,testing):
    args ={
        "testing": testing
    }
    return render(request, 'backpack/form_page.html', args)




