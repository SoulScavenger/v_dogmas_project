from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('registration/', views.CreateUser.as_view(), name='registration')
]
