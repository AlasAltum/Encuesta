from django.urls import path
from accounts import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('landing_page/', views.landing_page, name='landing_page'),
]