"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from firstapp import views
from MultiViewApp import views as v1
from django.urls import re_path
#App1
#approach-1
from App1 import views as v11
#approach-2
from App1.views import f11
#App2
#approach-1
from App2 import views as v22
#approach-2
from App2.views import f22


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.display),
    path('welcome2/',views.show),
    #path('hello/',views.hello),
    path('dtime/',views.disdatetime),
    
    #MultipleViewApp 
    path('mrng/',v1.f1),
    path('aftr/',v1.f2),
    path('evng/',v1.f3),
    
    #App1
    #approach-1&2
    path('hello/',v11.f11),
    path('hello/',f11),
    
    #App2
    #approach-1&2
    path('datetime/',v22.f22),
    path('datetime/',f22),
    
    #firstapp multi-url-req
    path('firstdemo/',views.demo),
    path('seconddemo/',views.demo),
    path('thirddemo/',views.demo),
    
    #default-url-url() or path()
	#path('$', views.homepage), 
	#path('.', views.homepage), 
	#path('^.*$', views.homepage), 
	re_path("^.*$",views.homepage),
	#url(r'$', views.homepage), 
	#url(r'^.*$', views.homepage),  #reqex-url-pattern
	
]
