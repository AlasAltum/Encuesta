from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_from_account, name='logout'),
    path('home/', views.home, name='home'),
    path('my_account/', views.my_account, name='my_account'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

