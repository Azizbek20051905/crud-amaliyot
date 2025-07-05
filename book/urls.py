from django.urls import path
from .views import home, add_book, update_book,delete_book

urlpatterns = [
    path("", home, name="home"),
    path("add/", add_book, name="add_book"),
    path("update/<int:id>", update_book, name="update"),
    path("delete/<int:id>", delete_book, name="delete")
]