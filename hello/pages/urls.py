"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register_submission/', views.register_submission, name='register_submission'),
    path('verify_login/', views.verify_login, name='verify_login'),
    path('sidelist/',views.sidelist,name='sidelist'),
    path('itemlist/',views.itemlist,name='itemlist'),
    path('about/',views.about,name='about'),
    path('addbook/',views.addbook,name='addbook'),
    path('mobile/',views.mobile,name='mobile'),
    path('log/',views.log,name='log'),
    path('mail/',views.mail,name='mail'),
    path('mob/',views.mob,name='mob'),
    path('last/',views.last,name='last'),
    path('register/',views.register,name='register'),
    path('register_d/',views.register_d,name='register_d'),
    path('last_submission/',views.last_submission,name='last_submission'),
    path('agents/',views.agents,name='agents'),
    path('update/',views.update,name='update'),
    path('prologin/',views.prologin,name='prologin'),
    path('proverify_login/',views.proverify_login,name='proverify_login'),
    path('cancel/',views.cancel,name='cancel'),
    path('cancelsub/',views.cancelsub,name='cancelsub'),
    path('ac/', views.ac, name='ac'),
    path('paint/', views.paint, name='paint'),
    path('lap/', views.lap, name='lap'),
    path('cctv/', views.cctv, name='cctv'),
    path('salon/', views.salon, name='salon'),
    path('pest/', views.pest, name='pest'),
    path('acc/', views.acc, name='acc'),
    path('elec/', views.elec, name='elec'),
    path('loginh/', views.loginh, name='loginh'),
    path('verify_loginh/', views.verify_loginh, name='verify_loginh'),
    path('feedback/', views.feedback, name='feedback'),


]
