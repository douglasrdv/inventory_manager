from django.urls import path
from . import views

urlpatterns = [path("", views.home, name="home"),
               path("index", views.index, name="index"),
               path("new-product", views.productRegistration, name="new-Product"),
               path("list", views.productRegistration, name="list")]
