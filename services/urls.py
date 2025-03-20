from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'services'

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
] 