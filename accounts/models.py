from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """نموذج الملف الشخصي للمستخدم"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    @classmethod
    def get_or_create_profile(cls, user):
        """
        الحصول على الملف الشخصي للمستخدم أو إنشاؤه إذا لم يكن موجودًا
        """
        try:
            return user.profile
        except cls.DoesNotExist:
            return cls.objects.create(user=user)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """إنشاء ملف شخصي تلقائياً عند إنشاء مستخدم جديد"""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """حفظ الملف الشخصي عند تحديث المستخدم"""
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
