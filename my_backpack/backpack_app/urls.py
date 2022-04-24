from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("library", views.library, name="library"),
    #path("<str:name>", views.greet, name="greet"),
    #this path is for add page
    path("add", views.add,  name="add"),
    #this path is add/CARDNAME which will use the cardname for parameter
    path("add/<str:card>", views.add, name="add"),
    
    path("forms", views.forms, name="forms")
    
]