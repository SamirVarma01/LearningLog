from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    #registration
    if request.method != 'POST':
        #blank registration form
        form = UserCreationForm()
    else:
        #process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log user in, redirect to home
            login(request, new_user)
            return redirect('learning_logs:index')

    #Display blank form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
