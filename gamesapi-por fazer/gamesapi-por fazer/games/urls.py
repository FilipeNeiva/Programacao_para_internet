"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.conf.urls import url
from games.views import *

urlpatterns = [
    path('games/', game_list),
    path('games/<int:id>', game_detail)
]
