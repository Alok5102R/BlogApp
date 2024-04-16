from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth, messages
import re
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from . import models
from django.core.paginator import Paginator
from django.db.models import Exists, OuterRef

# Create your views here.

User = get_user_model()

@login_required(login_url='signin') 
def home(request):
    blogs = models.Blog.objects.all().order_by('-created_at')
    blogs = blogs.annotate(blog_liked=Exists(
        models.Like.objects.filter(blog=OuterRef('blog_id'),user=request.user)
        ))
    paginator_object = Paginator(blogs, 5)
    try:
        page_no = request.GET['page_no']
    except:
        page_no = 1
    blogs_list = paginator_object.get_page(page_no)
    return render(request, 'index.html', {"blogs": blogs_list, "username":request.user.username})


@login_required(login_url='signin') 
def post_blog(request):
    if request.method == 'POST':
        blog = request.POST['blog']

        user = request.user
        blogProfile = models.Blog.objects.create(user=user, blog=blog)
        blogProfile.save()
    return redirect('/')


@login_required(login_url='signin')
def like_blog(request):
    user = request.user
    blog_id = request.GET['blog_id']
    page_no = request.GET['page_no']
    blog_data = models.Blog.objects.get(blog_id=blog_id)
    try:
        liked = models.Like.objects.get(blog=blog_data, user=user)
    except:
        liked = None
        
    if liked == None:
        newLike = models.Like.objects.create(blog=blog_data, user=user)
        blog_data.like_count += 1
        blog_data.save()
        newLike.save()
    else:
        liked.delete()
        blog_data.like_count -= 1
        blog_data.save()
    return redirect("/?page_no="+page_no)



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