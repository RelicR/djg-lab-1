from django.urls import path
from . import views


urlpatterns = [
    path('', views.index1, name='home'),
    path('about', views.about_us1, name='about'),
    path('examples', views.examples, name='examples')
]
'''
    path('create', views.create, name='create'),'''