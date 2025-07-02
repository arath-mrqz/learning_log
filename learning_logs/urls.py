"""Define the URLs for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    path('',views.index, name = 'index'),
    # the page that shows all the topics
    path('topics/', views.topics, name= 'topics'),
    # page for each topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]