from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """view method intermediator for the registration page"""
    # if there is no data yet to register
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)        
        if form.is_valid():
            new_user = form.save()
            # log the user in and then redirect to home
            login(request, new_user)
            return redirect('learning_logs:index')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)



