from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from .models import Service, ServiceCategory, Project

def services_list(request):
    """قائمة الخدمات"""
    categories = ServiceCategory.objects.all()
    services = Service.objects.all().order_by('category', 'order')
    featured_services = Service.objects.filter(featured=True).order_by('order')
    
    context = {
        'categories': categories,
        'services': services,
        'featured_services': featured_services,
    }
    return render(request, 'services/services_list.html', context)

def service_detail(request, slug):
    """تفاصيل الخدمة"""
    service = get_object_or_404(Service, slug=slug)
    related_services = Service.objects.filter(category=service.category).exclude(id=service.id).order_by('order')[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'services/service_detail.html', context)

def projects_list(request):
    """قائمة المشاريع"""
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(featured=True)
    statuses = dict(Project.STATUSES)
    
    context = {
        'projects': projects,
        'featured_projects': featured_projects,
        'statuses': statuses,
    }
    return render(request, 'services/projects_list.html', context)

def project_detail(request, slug):
    """تفاصيل المشروع"""
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(services__in=project.services.all()).distinct().exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'services/project_detail.html', context)
