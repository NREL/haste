from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('download', views.download, name='download'),
    path('site', views.site, name='site'),
    path('add_site', views.CreateSite.as_view(), name='add_site')
]
