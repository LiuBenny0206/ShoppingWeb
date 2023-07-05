from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .form import RegisterForm,LoginForm
# Create your views here.

@login_required(login_url="Login")
def home(request):
    return render(request,'BennyAgent/homepage.html')
def HermesClothing(request):
    return render(request, 'BennyAgent/HermesClothing.html')
def HermesHandbags(request):
    return render(request, 'BennyAgent/HermesHandbags.html')
def HermesShoes(request):
    return render(request, 'BennyAgent/HermesShoes.html')
def HermesAccessories(request):
    return render(request, 'BennyAgent/HermesAccessories.html')
def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Login')  # 根據你的URL配置，這裡應該是 'Login'
    context = {
        'form': form
    }
    return render(request, 'BennyAgent/registerweb.html', context)
def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('HomePage')
        else:
            error = "incorrect username or password"
    else:
        error = None

    context = {
        'form':form,
        'error': error
    }
    return render(request, 'BennyAgent/loginweb.html', context)
def log_out(request):
    logout(request)
    return redirect('Login')