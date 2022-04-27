from django.urls import path
from . import views

app_name = "backpack"
urlpatterns = [
    path("", views.index, name="index"),
    path("library", views.library, name="library")#,
    #path("<str:name>", views.greet, name="greet"),
    #this path is for add page
    #path("price/<str:name>", views.price, name="price"),
    #path("add", views.add,  name="add"),
    #this path is add/CARDNAME which will use the cardname for parameter
    #path("add/<str:card>", views.add, name="add"),    
    #path("forms", views.form, name="forms")
    
]