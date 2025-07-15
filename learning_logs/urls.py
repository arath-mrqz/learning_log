"""Define the URLs for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    path('',views.index, name = 'index'),
    # the page that shows all the topics
    path('topics/', views.topics, name= 'topics'),
    # page for each topic ans its entries
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # page for an user to enter a new topic
    path('new_topic/', views.new_topic, name= 'new_topic'),
    # page for an user to enter an entry
    path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
    # page for editing the entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    ]

