from django.urls import path
from . import views
urlpatterns=[
    path('',views.eazy_login),
    path('home',views.home),
    path('eazy_logout',views.eazy_logout),
    path('add_prod',views.add_prod),
    path('edit/<pid>',views.edit),
    path('delete/<pid>',views.delete),
]