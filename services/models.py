from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class ServiceCategory(models.Model):
    """فئات الخدمات"""
    name = models.CharField(_("الاسم"), max_length=100)
    slug = models.SlugField(_("الرابط المختصر"), unique=True)
    description = models.TextField(_("الوصف"))
    icon = models.CharField(_("أيقونة"), max_length=50, help_text=_("اسم أيقونة من Font Awesome"))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("فئة خدمات")
        verbose_name_plural = _("فئات الخدمات")

class Service(models.Model):
    """الخدمات المقدمة"""
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(_("العنوان"), max_length=200)
    slug = models.SlugField(_("الرابط المختصر"), unique=True)
    short_description = models.TextField(_("وصف مختصر"))
    description = models.TextField(_("الوصف التفصيلي"))
    main_image = models.ImageField(_("الصورة الرئيسية"), upload_to='services/')
    icon = models.CharField(_("أيقونة"), max_length=50, help_text=_("اسم أيقونة من Font Awesome"))
    featured = models.BooleanField(_("مميزة"), default=False)
    created_at = models.DateTimeField(_("تاريخ الإنشاء"), auto_now_add=True)
    updated_at = models.DateTimeField(_("تاريخ التحديث"), auto_now=True)
    order = models.IntegerField(_("الترتيب"), default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("خدمة")
        verbose_name_plural = _("الخدمات")
        ordering = ['order', '-updated_at']

class ServiceImage(models.Model):
    """صور إضافية للخدمات"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(_("الصورة"), upload_to='services/gallery/')
    title = models.CharField(_("العنوان"), max_length=100, blank=True)
    order = models.IntegerField(_("الترتيب"), default=0)
    
    class Meta:
        verbose_name = _("صورة الخدمة")
        verbose_name_plural = _("صور الخدمات")
        ordering = ['order']

class Project(models.Model):
    """المشاريع المنفذة"""
    STATUSES = (
        ('completed', _('مكتمل')),
        ('in_progress', _('قيد التنفيذ')),
        ('planned', _('مخطط له')),
    )
    
    title = models.CharField(_("العنوان"), max_length=200)
    slug = models.SlugField(_("الرابط المختصر"), unique=True)
    client = models.CharField(_("العميل"), max_length=100)
    location = models.CharField(_("الموقع"), max_length=100)
    start_date = models.DateField(_("تاريخ البدء"))
    end_date = models.DateField(_("تاريخ الانتهاء"), null=True, blank=True)
    status = models.CharField(_("الحالة"), max_length=20, choices=STATUSES)
    short_description = models.TextField(_("وصف مختصر"))
    description = models.TextField(_("الوصف التفصيلي"))
    main_image = models.ImageField(_("الصورة الرئيسية"), upload_to='projects/')
    services = models.ManyToManyField(Service, related_name='projects', verbose_name=_("الخدمات المرتبطة"))
    featured = models.BooleanField(_("مميز"), default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("مشروع")
        verbose_name_plural = _("المشاريع")
        ordering = ['-start_date']

class ProjectImage(models.Model):
    """صور إضافية للمشاريع"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(_("الصورة"), upload_to='projects/gallery/')
    title = models.CharField(_("العنوان"), max_length=100, blank=True)
    order = models.IntegerField(_("الترتيب"), default=0)
    
    class Meta:
        verbose_name = _("صورة المشروع")
        verbose_name_plural = _("صور المشاريع")
        ordering = ['order']
