from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserActionLog(models.Model):
    """سجل نشاطات المستخدمين في لوحة التحكم"""
    ACTION_TYPES = (
        ('create', _('إنشاء')),
        ('update', _('تعديل')),
        ('delete', _('حذف')),
        ('login', _('تسجيل دخول')),
        ('logout', _('تسجيل خروج')),
    )
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='actions')
    action_type = models.CharField(_("نوع النشاط"), max_length=20, choices=ACTION_TYPES)
    model_name = models.CharField(_("اسم النموذج"), max_length=100, blank=True)
    object_id = models.PositiveIntegerField(_("معرف الكائن"), null=True, blank=True)
    description = models.TextField(_("الوصف"))
    timestamp = models.DateTimeField(_("التوقيت"), auto_now_add=True)
    ip_address = models.GenericIPAddressField(_("عنوان IP"), null=True, blank=True)
    
    class Meta:
        verbose_name = _("سجل نشاط")
        verbose_name_plural = _("سجلات النشاطات")
        ordering = ['-timestamp']
