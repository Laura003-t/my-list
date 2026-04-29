from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Folder, List, ListMembers
from django.contrib import messages

# Create your views here.
# Get the user signed in
def current_user(request):
    """Fetching active session"""
    userid = request.session.get("userid")
    if not userid:
        return None
    return get_object_or_404(User, username=userid)

# Authentication -----------------------------------------------------------
def login(request):
    if request.session.get('userid'):
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        try:
            user = User.objects.get(username=userid)
            if user.password == password:
                request.session['userid'] = member.username
                return redirect('home')
            else:
                messages.error(request, 'Incorrect password. Please try again.')
        except User.DoesNotExist:
            messages.error(request, 'There is no user with that username.')
    return render(request, 'login.html')

def register(request):
    """This page is to create a user account"""
    if request.session.get('userid'):
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if not username:
            messages.error(request, 'You must provide a username')
        elif not email:
            messages.error(request, 'You must provide an email')
        elif not password:
            messages.error(request, 'You must enter a password')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'This username is taken')
        elif password1 != password2:
            messages.error(request, 'The passwords do not match')
        else:
            user = User.objects.create(
                username=username,
                email = email,
                password = password1,
            )
            messages.success(request, f'Your account has been successfully created, "{ username }".')
            return redirect('login')

        return render(request, 'register.html')

def logout(register):
    request.session.flush()
    return redirect('login')

