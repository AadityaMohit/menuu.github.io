"""
URL configuration for menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

admin.site.header="Developer Mohit"
admin.site.site_title="Welcome to Mohit Portal"
admin.site.index_title="Welcome to Mohit Portal"

urlpatterns = [
   path('', views.home, name='home'),
       path('home/', views.home, name='home'),
     path('about/', views.about, name='about'),
       path('contact/', views.contact, name='contact'),
         path('menu/', views.menu, name='menu'),
          path('meat/', views.meat, name='meat'),
          path('cake/', views.cake, name='cake'),
          path('snacks/', views.snacks, name='snacks'),
            path('form/', views.form, name='form'),
             path('redirect/', views.redirect, name='redirect'),
               path('redirect1/', views.redirect1, name='redirect1'),
             path('payment/', views.payment, name='payment'),
               path('cardpage/', views.cardpage, name='cardpage'),
   
]
