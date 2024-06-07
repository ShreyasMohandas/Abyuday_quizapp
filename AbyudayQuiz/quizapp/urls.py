from django.urls import path
from quizapp import views

app_name = 'quizapp'

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('login/',views.user_login,name='login'),
    path('register/',views.user_register,name='register'),
    path('logout/',views.user_logout,name='logout'),
]