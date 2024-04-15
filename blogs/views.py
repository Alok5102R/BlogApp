from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth, messages
import re
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.

User = get_user_model()

@login_required(login_url='signin') 
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        check_strength = password_criteria_check(password)
        
        if len(str(username)) == 0 or len(str(email)) == 0 or len(str(password)) == 0 or len(str(password2)) == 0:
            messages.info(request, 'All Fields are required!!')
        elif len(str(email).split('@')[-1].split('.')) <= 1:
            messages.info(request, 'Enter correct email address!!')
        elif len(str(password)) < 9:
            messages.info(request, 'Password length should be greater than 8 characters!!')
        elif check_strength == False:
            messages.info(request, 'Password should contain: Uppercase, Lowercase, Digit and Special character!!')
        elif password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use!!')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!!')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)                     # Log user in and redirect to settings page 
                return redirect('/')
        else:
            messages.info(request, 'Passwords does not match!!')
            return redirect('signup')
    return render(request, 'signup.html')

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password!!')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
    

@login_required(login_url='signin') 
def logout(request):
    auth.logout(request)
    return redirect('signin')

# ========== Extras ==========

def password_criteria_check(password):
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special_char = bool(re.search(r'[^A-Za-z0-9]', password))

    if has_upper and has_lower and has_digit and has_special_char:
        return True
    else:
        return False