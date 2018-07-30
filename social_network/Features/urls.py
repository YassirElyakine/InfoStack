from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('<category>/topics', views.category, name='category'),
    path('newpost/', views.newpost, name='newpost'),
    path('<category>/topics/<posttitle>', views.view_post, name='viewpost'),
]