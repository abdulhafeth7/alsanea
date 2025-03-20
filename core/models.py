from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class SiteSettings(models.Model):
    """إعدادات الموقع العامة"""
    site_name = models.CharField(_("اسم الموقع"), max_length=100)
    site_title = models.CharField(_("عنوان الموقع"), max_length=200)
    site_description = models.TextField(_("وصف الموقع"))
    contact_email = models.EmailField(_("البريد الإلكتروني للتواصل"))
    contact_phone = models.CharField(_("رقم الهاتف"), max_length=20)
    address = models.TextField(_("العنوان"))
    facebook_url = models.URLField(_("رابط فيسبوك"), blank=True)
    twitter_url = models.URLField(_("رابط تويتر"), blank=True)
    linkedin_url = models.URLField(_("رابط لينكد إن"), blank=True)
    instagram_url = models.URLField(_("رابط إنستجرام"), blank=True)
    youtube_url = models.URLField(_("رابط يوتيوب"), blank=True)
    footer_text = models.TextField(_("نص التذييل"))
    google_analytics = models.TextField(_("كود جوجل أناليتكس"), blank=True)
    
    class Meta:
        verbose_name = _("إعدادات الموقع")
        verbose_name_plural = _("إعدادات الموقع")

class CompanyInfo(models.Model):
    """معلومات الشركة"""
    vision = models.TextField(_("الرؤية"))
    mission = models.TextField(_("الرسالة"))
    history = models.TextField(_("تاريخ الشركة"))
    about_image = models.ImageField(_("صورة تعريفية"), upload_to='company/')
    
    class Meta:
        verbose_name = _("معلومات الشركة")
        verbose_name_plural = _("معلومات الشركة")

class TeamMember(models.Model):
    """أعضاء مجلس الإدارة والفريق"""
    name = models.CharField(_("الاسم"), max_length=100)
    position = models.CharField(_("المنصب"), max_length=100)
    bio = models.TextField(_("نبذة مختصرة"))
    image = models.ImageField(_("الصورة"), upload_to='team/')
    is_board_member = models.BooleanField(_("عضو مجلس إدارة"), default=False)
    order = models.IntegerField(_("الترتيب"), default=0)
    
    class Meta:
        verbose_name = _("عضو الفريق")
        verbose_name_plural = _("أعضاء الفريق")
        ordering = ['order', 'name']

class Testimonial(models.Model):
    """آراء العملاء"""
    name = models.CharField(_("الاسم"), max_length=100)
    position = models.CharField(_("المنصب"), max_length=100)
    company = models.CharField(_("الشركة"), max_length=100)
    testimonial = models.TextField(_("الشهادة"))
    image = models.ImageField(_("الصورة"), upload_to='testimonials/', blank=True)
    is_active = models.BooleanField(_("نشط"), default=True)
    
    class Meta:
        verbose_name = _("رأي عميل")
        verbose_name_plural = _("آراء العملاء")

class ContactMessage(models.Model):
    """رسائل التواصل"""
    name = models.CharField(_("الاسم"), max_length=100)
    email = models.EmailField(_("البريد الإلكتروني"))
    phone = models.CharField(_("رقم الهاتف"), max_length=20)
    subject = models.CharField(_("الموضوع"), max_length=200)
    message = models.TextField(_("الرسالة"))
    created_at = models.DateTimeField(_("تاريخ الإرسال"), auto_now_add=True)
    is_read = models.BooleanField(_("تمت القراءة"), default=False)
    
    class Meta:
        verbose_name = _("رسالة تواصل")
        verbose_name_plural = _("رسائل التواصل")
        ordering = ['-created_at']

class Partner(models.Model):
    """الشركاء والعملاء"""
    name = models.CharField(_("الاسم"), max_length=100)
    logo = models.ImageField(_("الشعار"), upload_to='partners/')
    website = models.URLField(_("الموقع الإلكتروني"), blank=True)
    is_partner = models.BooleanField(_("شريك"), default=True)
    
    class Meta:
        verbose_name = _("شريك/عميل")
        verbose_name_plural = _("الشركاء والعملاء")

class Slider(models.Model):
    """شرائح العرض الرئيسية"""
    title = models.CharField(_("العنوان"), max_length=200)
    subtitle = models.CharField(_("العنوان الفرعي"), max_length=300, blank=True)
    description = models.TextField(_("الوصف"), blank=True)
    image = models.ImageField(_("الصورة"), upload_to='sliders/')
    button_text = models.CharField(_("نص الزر"), max_length=50, blank=True)
    button_url = models.CharField(_("رابط الزر"), max_length=200, blank=True)
    order = models.IntegerField(_("الترتيب"), default=0)
    is_active = models.BooleanField(_("نشط"), default=True)
    
    class Meta:
        verbose_name = _("شريحة عرض")
        verbose_name_plural = _("شرائح العرض")
        ordering = ['order']
