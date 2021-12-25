"""bettsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from England.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/', include('API.api-url')),

    path('admin/', admin.site.urls),
    path('login/',login_view,name='login'),
    path('room/', room_view, name='room'),
    path('home/', home_view.as_view(), name='home'),
    #path('club/<str:id>/', club_view, name='club'),
   ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)