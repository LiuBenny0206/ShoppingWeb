from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= 'HomePage'),
    path('register', views.sign_up, name= 'Register'),
    path('login',views.sign_in, name= 'Login'),
    path('HermesClothing', views.HermesClothing, name= 'HermesClothing'),
    path('HermesHandbags', views.HermesHandbags, name= 'HermesHandbags'),
    path('HermesShoes', views.HermesShoes, name= 'HermesShoes'),
    path('HermesAccessories', views.HermesAccessories, name='HermesAccessories'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
