from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        passwordcon = request.POST['passwordCon']
        email = request.POST['email']
        
        if password == passwordcon:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already registered')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username,
                                                password=password,
                                                email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                return redirect('/')
        else:
            messages.info(request,'passwords are not matched')
            return redirect('register')
    else:
        return render(request,'sign_up.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['user_pass']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'sign_in.html')
