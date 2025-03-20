from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """نموذج صفحة الاتصال"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('الاسم الكامل')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('البريد الإلكتروني')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('رقم الهاتف')}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('موضوع الرسالة')}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': _('نص الرسالة')}),
        } 