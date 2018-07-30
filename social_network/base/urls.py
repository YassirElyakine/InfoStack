from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', include('Authentication.urls')),
    path('account/', include('Features.urls')),
    path('', include('Features.urls')),
]