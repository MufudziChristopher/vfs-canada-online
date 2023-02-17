from django.urls import path

from . import views

app_name = "app"


urlpatterns = [
    #Leave as empty string for base url

    #------------ (STORE - URLS) ------------

	path('', views.landing, name="landing"),
	path('home', views.home, name="home"),
	path('track/', views.track, name="track"),
	path('contact/', views.contact, name="contact"),

]
