from django.urls import path
from . import views

app_name = 'accurl'
urlpatterns = [
 path('signup/', views.signupView, name='signup'),
 path('login/', views.loginView, name='login'),
 path('logout/', views.mylogout, name='logout'),
 path('profile/', views.mydash, name='profile'),
 ]