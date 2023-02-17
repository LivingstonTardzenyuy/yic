from django.urls import path
from . import views


urlpatterns= [
    path('',views.home,name='home'),
    path('business',views.business,name='business'),
    path('contact',views.contact,name='contact'),
    path('courses',views.courses,name='courses'),
    path('books',views.books,name='books'),
    
]