from django.urls import include, path

from command import views

app_name = 'command'

commands_url = [
    path(
        '<int:pk>/', views.CommandDetailView.as_view(), name='detail'
    ),
    path(
        'create/', views.CommandCreateView.as_view(), name='create'
    ),
    path(
        '<int:pk>/edit/', views.CommandUpdateView.as_view(), name='edit'
    ),
    path(
        '<int:pk>/delete/', views.CommandDeleteView.as_view(), name='delete'
    ),
]

urlpatterns = [
    path('', views.CommandListView.as_view(), name='index'),
    path('commands/', include(commands_url)),
    path('tags/<slug:tag_slug>/', views.TagDetailView.as_view(), name='tag')
]
