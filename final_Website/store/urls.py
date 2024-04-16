from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutor/', views.tutor, name='tutor'),
    path('class/', views.classes, name='class'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

]
