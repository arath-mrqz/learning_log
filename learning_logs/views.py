from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    """page for entering a new topic by the user"""
    if request.method != 'POST':
    #  no data submitted; create a blank form
        form = TopicForm()

    else:
    #  POST data submitted, process the data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """page for entering a new entry in the topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
    #  no data submitted; create a blankd form
        form = EntryForm()
    else:
    #  POST data submitted, process the data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return redirect('learning_logs:topic', topic_id=topic.id)
    
    # display a blank or invalid form

    context = {'form':form,
               'topic':topic}
    
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """page for editing an entry"""

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic


    if request.method != 'POST':
        # initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)

    else:
        # POST data submmited, process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic.id)

    context = {'entry': entry,
               'form' : form,
               'topic': topic}

    return render(request, 'learning_logs/edit_entry.html', context)