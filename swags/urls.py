from django.urls import path

from swags import views

urlpatterns = [
    path('', views.swags, name='swags')
]
