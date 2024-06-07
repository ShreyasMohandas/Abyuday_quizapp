from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from quizapp.forms import CreateUser

# Create your views here.
class IndexView(LoginRequiredMixin,TemplateView):
    template_name='quizapp/home.html'


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password1')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("quizapp:home")
        else:
            messages.info(request,"Username or Password is incorrect")
    return render(request,'quizapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('quizapp:login')

def user_register(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quizapp:login')
    
    return render(request,'quizapp/register.html',context={'form':form})