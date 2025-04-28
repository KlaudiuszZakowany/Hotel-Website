from django.urls import path
from .views import ProfilePageView, CustomerSignUpView, ManagerSignUpView, EmployeeSignUpView

app_name = 'accounts'

urlpatterns = [
    path('c_signup/', CustomerSignUpView.as_view(), name='csignup'),
    path('m_signup/', ManagerSignUpView.as_view(), name='msignup'),
    path('e_signup/', EmployeeSignUpView.as_view(), name='esignup'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
] 