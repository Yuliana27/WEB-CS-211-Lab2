from django.contrib import admin
from django.urls import path, re_path
from cupcakes import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('dishes/',  views.list_dishes),
    re_path('dishes/(?P<code>\w+)/$', views.dish_details),
    path('index/', views.client),
    path('index/menu.html/', views.menu),
    path('index/login.html/', views.login),
    path('index/registration.html/', views.registration),
    path('calls/',  views.list_calls),
    re_path('calls/(?P<pk>\d+)/$', views.call_details),
    path('list.html/',  views.list),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)