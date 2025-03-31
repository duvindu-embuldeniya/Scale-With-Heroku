from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm, ThoughtForm, UserUpdateForm, ProfileUpateForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Thought

def home(request):
    return render(request, 'home/index.html')

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request, new_user)
            messages.success(request, 'Account Created Successfully!')
            return redirect('dashboard')
    context ={'form':form}  
    return render(request, 'home/register.html', context)

def login(request):
    if request.user.is_authenticated:
        messages.info(request, "You've already Loged-in!")
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_user = auth.authenticate(username = username, password = password)
        if auth_user is not None:
            auth.login(request, auth_user)
            messages.success(request, 'Successfully Loged-in!')
            return redirect('dashboard')
        else:
            messages.error(request, "User doesn't Exist!")
            return redirect('login')
    return render(request, 'home/login.html')

def logout(request):
    if not(request.user.is_authenticated):
        messages.info(request, "You've not Logged-in!")
        return redirect('home')
    auth.logout(request)
    messages.success(request, 'Successfully Loged-out!')
    return redirect('home')


@login_required
def dashboard(request):
    thoughts = Thought.objects.all()
    context = {'thoughts':thoughts}
    return render(request, 'home/dashboard.html', context)

@login_required
def myThoughts(request, username):
    usr = User.objects.get(username = username)
    thoughts = usr.thought_set.all()
    context = {'thoughts':thoughts}
    return render(request, 'home/thoughts_mine.html', context)

@login_required
def createThought(request):
    form = ThoughtForm()
    if request.method == 'POST':
        form = ThoughtForm(request.POST)
        if form.is_valid():
            new_thought = form.save(commit=False)
            new_thought.author = request.user
            new_thought.save()
            messages.success(request, 'Thought Created Sucessfully!')
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'home/thought_form.html', context)

@login_required
def updateThought(request, pk):
    thought = Thought.objects.get(pk = pk)
    if thought.author != request.user:
        return HttpResponse('<h1>403!</h1>')
    form = ThoughtForm(instance=thought)
    if request.method == 'POST':
        form = ThoughtForm(request.POST, instance=thought)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thought updated successfully!')
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'home/thought_form.html', context)


@login_required
def deleteThought(request, pk):
    thought = Thought.objects.get(pk = pk)
    if thought.author != request.user:
        return HttpResponse('<h1>403!</h1>')
    if request.method == 'POST':
        thought.delete()
        messages.success(request, 'Thought deleted successfully!')
        return redirect('dashboard')
    context = {'thought':thought}
    return render(request, 'home/thought_delete.html', context)



@login_required
def profile(request, username):
    usr = User.objects.get(username = username)
    if usr != request.user:
        return HttpResponse('<h1>403!</h1>')
    u_form = UserUpdateForm(instance=usr)
    p_form = ProfileUpateForm(instance=usr.profile)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=usr)
        p_form = ProfileUpateForm(request.POST, request.FILES, instance=usr.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('dashboard')
    context = {'usr':usr, 'u_form':u_form, 'p_form':p_form}
    return render(request, 'home/profile.html', context)


@login_required
def deleteProfile(request, pk):
    usr = User.objects.get(id = pk)
    if usr != request.user:
        return HttpResponse('<h1>403</h1>')
    if request.method == 'POST':
        usr.delete()
        messages.success(request, 'Account deleted successfully!')
        return redirect('dashboard')
    context = {'usr':usr}
    return render(request, 'home/delete_profile.html', context)