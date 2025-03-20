from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

@login_required
def profile(request):
    """عرض الملف الشخصي للمستخدم"""
    # التأكد من أن المستخدم لديه ملف شخصي
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    return render(request, 'accounts/profile.html')

@login_required
def profile_update(request):
    """تحديث الملف الشخصي للمستخدم"""
    # التأكد من أن المستخدم لديه ملف شخصي
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        user = request.user
        
        # تحديث بيانات المستخدم
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        
        # تحديث الملف الشخصي
        if 'profile_image' in request.FILES:
            profile.image = request.FILES['profile_image']
        profile.phone = request.POST.get('phone', profile.phone)
        profile.bio = request.POST.get('bio', profile.bio)
        profile.save()
        
        messages.success(request, 'تم تحديث الملف الشخصي بنجاح.')
        return redirect('accounts:profile')
    
    return render(request, 'accounts/profile_update.html')
