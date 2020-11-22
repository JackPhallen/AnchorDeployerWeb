from django.urls import path

from . import views

urlpatterns = [
    path('deploy', views.deploy_view, name='deploy'),
    path('check', views.check_view, name='check1'),
    path('getip', views.getip, name='getip')
]
