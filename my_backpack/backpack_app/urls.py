from django.urls import path
from . import views

app_name = "backpack"

urlpatterns = [
    path("", views.index, name="index"),
    path("library", views.library, name="library"),
    path("color", views.color, name="color"),
    path("price", views.price, name="price"),
    path("resources", views.resources, name="resources"),
    #path("add", views.add,  name="add"),
    #this path is add/CARDNAME which will use the cardname for parameter
    #path("add/<str:card>", views.add, name="add"),    
    path("form_page/<str:testing>", views.form_page, name="form_page")
    
]