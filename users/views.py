from django.shortcuts import render,redirect
from .forms import UserRegisterForm
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from django.contrib.auth.decorators import login_required
def register(requesst):
    if requesst.method == 'POST':
        form=UserRegisterForm(requesst.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
        return render(requesst,'register.html',{'form':form})


@login_required
def profile(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        form = PostForm()
    return render(request,'profile.html',{'form':form})