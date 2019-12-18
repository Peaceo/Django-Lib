"""library URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from  BookManage.views import viewBook, deleteBook, myBook, details, detail, new, forms, edit, update, signup

if settings.DEBUG:
    urlpatterns =   static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewBook/', viewBook),
    path('deleteBook/<int:book_id>/', deleteBook),
    path('myBook/', myBook),
    path('details/<int:book_id>/', details, name = 'details'),
    path('detail/<int:book_id>/', detail, name = 'detail'),   
    path('new/', new),
    path('forms/', forms),
    path('edit/<int:book_id>/', edit, name='edit'),
    path('update/<int:book_id>/', update, name = 'update'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    

]






  
