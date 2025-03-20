from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile

class Command(BaseCommand):
    help = 'إنشاء ملفات شخصية للمستخدمين الذين لا يملكون ملفات شخصية'

    def handle(self, *args, **kwargs):
        users_without_profile = []
        
        # البحث عن المستخدمين بدون ملفات شخصية
        for user in User.objects.all():
            try:
                # محاولة الوصول إلى الملف الشخصي
                profile = user.profile
            except Profile.DoesNotExist:
                # إذا لم يكن موجودًا، إضافة المستخدم إلى القائمة
                users_without_profile.append(user)
        
        # إنشاء ملفات شخصية للمستخدمين الذين لا يملكون ملفات شخصية
        for user in users_without_profile:
            Profile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'تم إنشاء ملف شخصي للمستخدم: {user.username}'))
        
        if not users_without_profile:
            self.stdout.write(self.style.SUCCESS('جميع المستخدمين لديهم ملفات شخصية.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'تم إنشاء {len(users_without_profile)} ملف شخصي.')) 