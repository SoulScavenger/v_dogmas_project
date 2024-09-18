
from django.urls import include, path, re_path

from api import views

app_name = 'api'

urlpatterns = [
    path('commands/', views.CommandAPIView.as_view()),
    path('commands/<int:pk>/', views.CommandAPIRetrieve.as_view()),
    path('commands/create/', views.CommandAPICreate.as_view()),
    path('commands/<int:pk>/update/', views.CommandAPIUpdate.as_view()),
    path('commands/<int:pk>/delete/', views.CommandAPIDestroy.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
