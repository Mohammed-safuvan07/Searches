from django.urls import path

from . import views

urlpatterns = [

    path('',views.searchs,name='search_view'),
]
