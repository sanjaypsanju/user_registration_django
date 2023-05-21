from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.urls import reverse
from reg.forms import CustomUserCreationForm
# Create your views here.
def register_view(request):
    form = CustomUserCreationForm()
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('register'))
    return render(request,'reg/register.html',{'form': form})