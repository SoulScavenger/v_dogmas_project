from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from command import views


router = routers.DefaultRouter()
router.register(r'commands', views.CommandAPIView)

api_urlpatterns = [
    path('', include('rest_framework.urls')),
    path('commands/', views.CommandAPIView.as_view()),
    path('commands/<int:pk>/', views.CommandAPIRetrieve.as_view()),
    path('commands/create/', views.CommandAPICreate.as_view()),
    path('commands/<int:pk>/update/', views.CommandAPIUpdate.as_view()),
    path('commands/<int:pk>/delete/', views.CommandAPIDestroy.as_view()),
    path('auth/', include('djoser.urls')),

]

urlpatterns = [
    path('', include('command.urls', namespace='command')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration/', include('user.urls', namespace='user')),
    path('api/v1/', include(api_urlpatterns)),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
