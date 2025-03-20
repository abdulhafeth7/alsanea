from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from core.models import *
from services.models import *
from .models import UserActionLog

@login_required
def dashboard(request):
    """لوحة التحكم الرئيسية"""
    # إحصائيات عامة
    stats = {
        'services_count': Service.objects.count(),
        'projects_count': Project.objects.count(),
        'team_count': TeamMember.objects.count(),
        'partners_count': Partner.objects.count(),
        'messages_count': ContactMessage.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count(),
    }
    
    # آخر الرسائل
    recent_messages = ContactMessage.objects.all().order_by('-created_at')[:5]
    
    # آخر النشاطات
    recent_activities = UserActionLog.objects.filter(user=request.user).order_by('-timestamp')[:10]
    
    context = {
        'stats': stats,
        'recent_messages': recent_messages,
        'recent_activities': recent_activities,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def content_manager(request):
    """إدارة المحتوى"""
    context = {
        'services': Service.objects.all().order_by('category', 'order'),
        'projects': Project.objects.all().order_by('-start_date'),
        'sliders': Slider.objects.all().order_by('order'),
    }
    return render(request, 'dashboard/content_manager.html', context)

@login_required
def media_manager(request):
    """إدارة الوسائط"""
    context = {}
    return render(request, 'dashboard/media_manager.html', context)

@login_required
def users_manager(request):
    """إدارة المستخدمين"""
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'dashboard/users_manager.html', context)

@login_required
def settings(request):
    """إعدادات الموقع"""
    site_settings = SiteSettings.objects.first()
    company_info = CompanyInfo.objects.first()
    
    context = {
        'site_settings': site_settings,
        'company_info': company_info,
    }
    return render(request, 'dashboard/settings.html', context)
