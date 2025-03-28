from django.urls import path
from .views import SignUpView, ProfilePageView

app_name = 'accounts'

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile')
] 