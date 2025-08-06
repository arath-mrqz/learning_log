"""defines the urls for the accounts app"""

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # include default auth urls
    path('', include('django.contrib.auth.urls')),
    # registration url pattern
    path('accounts/register/', views.register, name='register'),
]