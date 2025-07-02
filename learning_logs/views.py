from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """the home page for Learning Logs app"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """the topics page for that displays the data"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """page for each topic"""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    
    return render(request, 'learning_logs/topic.html', context)
