from django.urls import path
from .views import *
urlpatterns = [

    path('', Index.as_view(), name='home'),
    path('form/', MakeData.as_view(), name='post'),
    path('show/', Show.as_view(), name='show'),
]
