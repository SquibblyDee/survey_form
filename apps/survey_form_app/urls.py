from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    #Root route to our index page
    url(r'^$', views.index),
    #Route to the results page
    url(r'^result', views.result),
    #Route where all processing takes place, called by the button on index.html
    url(r'^process', views.process),
]