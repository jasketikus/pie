from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *

class HomePage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return render(request, 'pieapp/index.html')
    
class ProfilePage(LoginRequiredMixin, View):
    template_name = 'pieapp/profile.html'
    raise_exception = True
    def get(self, request):
        characteristics = Characteristic.objects.all()
        return render(request, 'pieapp/profile.html', {'characteristics': characteristics})

class RegisterPage(CreateView):
    form_class = RegisterUserForm
    template_name = 'pieapp/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginPage(LoginView):
    form_class = LoginUserForm
    template_name = 'pieapp/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')