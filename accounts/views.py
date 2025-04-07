from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .forms import CustomUserCreationForm
from .models import CustomUser, Profile

# Create your views here.

class CustomerSignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('get_booking')
    def form_valid(self, form):

    # Save the new user
        response = super().form_valid(form)
        # Add user to the Customer group
        customer_group, created = Group.objects.get_or_create(name='Customer')
        self.object.groups.add(customer_group)
        return response # Redirect to success URL


class ManagerSignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('get_booking')
    def form_valid(self, form):
        # Save the new user
        response = super().form_valid(form)
        # Add user to the Customer group
        customer_group, created = Group.objects.get_or_create(name='Manager')
        self.object.groups.add(customer_group)
        return response # Redirect to success URL

class EmployeeSignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('get_booking')
    def form_valid(self, form):
        # Save the new user
        response = super().form_valid(form)
        # Add user to the Customer group
        customer_group, created = Group.objects.get_or_create(name='Employee')
        self.object.groups.add(customer_group)
        return response # Redirect to success URL

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
