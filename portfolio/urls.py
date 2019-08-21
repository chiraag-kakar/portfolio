"""portfolio URL Configuration

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
from contents import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('certification/<int:pk>/', views.certification, name='certification'),
    path('project-document/<int:pk>/', views.project_document, name='project_document'),
    path('resume/<int:pk>/', views.resume, name='resume'),
    path('seminar/<int:pk>/', views.seminar, name='seminar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
