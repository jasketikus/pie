from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
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
            title = 'PIE constructor app'
            return render(request, 'pieapp/index.html', {'title': title})
    
class ProfilePage(LoginRequiredMixin, View):
    template_name = 'pieapp/profile.html'
    raise_exception = True
    def get(self, request):
        characteristics = Characteristic.objects.filter(user=request.user)
        char_rating = {char.name: char.rating for char in characteristics}
        my_graph = graph.create_graph(**char_rating)
        title = f'PIE app: {str(self.request.user)} - characteristics'
        return render(
            request, 
            'pieapp/profile.html', 
            {'characteristics': characteristics, 'graph': my_graph, 'title': title}
            )

class RegisterPage(CreateView):
    form_class = RegisterUserForm
    template_name = 'pieapp/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context

class LoginPage(LoginView):
    form_class = LoginUserForm
    template_name = 'pieapp/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Log in PIE app'
        return context


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
        context ['title'] = 'Add new characteristic PIE app'
        return context

class CharacteristicDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Characteristic
    template_name = 'pieapp/characteristic_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characteristics'] = Characteristic.objects.filter(user=self.request.user)
        context['title'] = f'{self.get_object().name} characteristic PIE app'
        return context

    def test_func(self):
        characteristic = self.get_object()
        return self.request.user == characteristic.user

class CharacteristicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Characteristic
    template_name = 'pieapp/addchar.html'
    form_class = AddCharacteristicForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characteristics'] = Characteristic.objects.filter(user=self.request.user)
        context['title'] = f'{self.get_object().name} update PIE app'
        return context
    
    def test_func(self):
        characteristic = self.get_object()
        return self.request.user == characteristic.user

class CharacteristicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Characteristic
    template_name = 'pieapp/delchar.html'
    success_url = '/profile'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characteristics'] = Characteristic.objects.filter(user=self.request.user)
        context['title'] = f'{self.get_object().name} delete PIE app'
        return context

    def test_func(self):
        characteristic = self.get_object()
        return self.request.user == characteristic.user
