"""gi_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from gi_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Contact_BookView.as_view(),name="contact_book"),
    path('add-contacts', Add_ContactView.as_view(),name="add_contact"),
    path('edit-contacts/<int:contact_id>', Edit_ContactView.as_view(),name="edit_contact"),
    path('delete-contacts', Delete_ContactView.as_view(),name="delete_contact"),
    path('view-contacts/<int:contact_id>', View_ContactView.as_view(),name="view_contact"),
    
    # path('',include([
    #     path('',Contact_BookView.as_view(),name='contact_book' ),
    # ])),

]
