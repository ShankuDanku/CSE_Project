from django.urls import path
from . import views
urlpatterns=[path('',views.HomePage,name='Crawler'),
             path('about/',views.about,name='about-guide')]