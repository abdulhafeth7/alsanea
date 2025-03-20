from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import Slider, CompanyInfo, TeamMember, Partner, ContactMessage
from .forms import ContactForm

def home(request):
    """الصفحة الرئيسية"""
    sliders = Slider.objects.filter(is_active=True).order_by('order')
    
    context = {
        'sliders': sliders,
    }
    return render(request, 'core/index.html', context)

def about(request):
    """صفحة عن الشركة"""
    company_info = CompanyInfo.objects.first()
    
    context = {
        'company_info': company_info,
    }
    return render(request, 'core/about.html', context)

def team(request):
    """صفحة فريق العمل"""
    board_members = TeamMember.objects.filter(is_board_member=True).order_by('order')
    team_members = TeamMember.objects.filter(is_board_member=False).order_by('order')
    
    context = {
        'board_members': board_members,
        'team_members': team_members,
    }
    return render(request, 'core/team.html', context)

def partners(request):
    """صفحة الشركاء والعملاء"""
    partners_list = Partner.objects.filter(is_partner=True)
    clients_list = Partner.objects.filter(is_partner=False)
    
    context = {
        'partners': partners_list,
        'clients': clients_list,
    }
    return render(request, 'core/partners.html', context)

def contact(request):
    """صفحة اتصل بنا"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('تم إرسال رسالتك بنجاح! سنتواصل معك قريباً.'))
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)
