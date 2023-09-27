"""
URL configuration for TransitInsights project.

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
from django.urls import path, include
from DashBoard.views import *

appname = "DashBoard"

urlpatterns = [
    # path('', DashBoard, name='DashBoard'),
    path('', D_Third, name='D_Third'),
    # path('D_Second/', D_Second, name='D_Second'),
    # path('D_Third/',D_Third, name='D_Third'),
    path('D_Fourth/',D_Fourth, name='D_Fourth'),
    path('D_Fivth/',D_Fivth,name="D_Fivth")
]
