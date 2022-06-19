from django.urls import path
from . import views

app_name = "backpack"

urlpatterns = [
    path("", views.index, name="index"),
    path("library", views.library, name="library"),
    path('add', views.add, name="add"),
    path("color", views.color, name="color"),
    path("price", views.price, name="price"),
    path("resources", views.resources, name="resources"),
    path('purchase', views.purchase, name="purchase"),  
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),  
    path("form_page/<str:testing>", views.form_page, name="form_page")
    
]