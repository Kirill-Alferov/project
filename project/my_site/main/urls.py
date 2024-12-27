from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index ),
    path('page', views.page ),
    path('pagea', views.pagea ),
    path('pageb', views.pageb )
]