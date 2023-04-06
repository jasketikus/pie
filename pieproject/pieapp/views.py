from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import *
from .models import *
from . import graph

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
        characteristics = Characteristic.objects.filter(user=request.user)
        my_graph = graph.create_graph()
        return render(request, 'pieapp/profile.html', {'characteristics': characteristics, "graph": my_graph})

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

class AddCharacteristic(CreateView):
    form_class = AddCharacteristicForm
    template_name = 'pieapp/addchar.html'
    
    def form_valid(self, form):
        characteristic = form.save(commit=False)
        characteristic.user = self.request.user
        characteristic.save()
        return redirect('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characteristics'] = Characteristic.objects.filter(user=self.request.user)
        return context

class CharacteristicDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Characteristic
    template_name = 'pieapp/characteristic_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characteristics'] = Characteristic.objects.filter(user=self.request.user)
        return context

    def test_func(self):
        characteristic = self.get_object()
        return self.request.user == characteristic.user
    
