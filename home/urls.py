from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('answer/', views.answer, name='answer')
]
