# Generated by Django 3.2.25 on 2025-03-18 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vision', models.TextField(verbose_name='الرؤية')),
                ('mission', models.TextField(verbose_name='الرسالة')),
                ('history', models.TextField(verbose_name='تاريخ الشركة')),
                ('about_image', models.ImageField(upload_to='company/', verbose_name='صورة تعريفية')),
            ],
            options={
                'verbose_name': 'معلومات الشركة',
                'verbose_name_plural': 'معلومات الشركة',
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الاسم')),
                ('email', models.EmailField(max_length=254, verbose_name='البريد الإلكتروني')),
                ('phone', models.CharField(max_length=20, verbose_name='رقم الهاتف')),
                ('subject', models.CharField(max_length=200, verbose_name='الموضوع')),
                ('message', models.TextField(verbose_name='الرسالة')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإرسال')),
                ('is_read', models.BooleanField(default=False, verbose_name='تمت القراءة')),
            ],
            options={
                'verbose_name': 'رسالة تواصل',
                'verbose_name_plural': 'رسائل التواصل',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الاسم')),
                ('logo', models.ImageField(upload_to='partners/', verbose_name='الشعار')),
                ('website', models.URLField(blank=True, verbose_name='الموقع الإلكتروني')),
                ('is_partner', models.BooleanField(default=True, verbose_name='شريك')),
            ],
            options={
                'verbose_name': 'شريك/عميل',
                'verbose_name_plural': 'الشركاء والعملاء',
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100, verbose_name='اسم الموقع')),
                ('site_title', models.CharField(max_length=200, verbose_name='عنوان الموقع')),
                ('site_description', models.TextField(verbose_name='وصف الموقع')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='البريد الإلكتروني للتواصل')),
                ('contact_phone', models.CharField(max_length=20, verbose_name='رقم الهاتف')),
                ('address', models.TextField(verbose_name='العنوان')),
                ('facebook_url', models.URLField(blank=True, verbose_name='رابط فيسبوك')),
                ('twitter_url', models.URLField(blank=True, verbose_name='رابط تويتر')),
                ('linkedin_url', models.URLField(blank=True, verbose_name='رابط لينكد إن')),
                ('instagram_url', models.URLField(blank=True, verbose_name='رابط إنستجرام')),
                ('youtube_url', models.URLField(blank=True, verbose_name='رابط يوتيوب')),
                ('footer_text', models.TextField(verbose_name='نص التذييل')),
                ('google_analytics', models.TextField(blank=True, verbose_name='كود جوجل أناليتكس')),
            ],
            options={
                'verbose_name': 'إعدادات الموقع',
                'verbose_name_plural': 'إعدادات الموقع',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='العنوان')),
                ('subtitle', models.CharField(blank=True, max_length=300, verbose_name='العنوان الفرعي')),
                ('description', models.TextField(blank=True, verbose_name='الوصف')),
                ('image', models.ImageField(upload_to='sliders/', verbose_name='الصورة')),
                ('button_text', models.CharField(blank=True, max_length=50, verbose_name='نص الزر')),
                ('button_url', models.CharField(blank=True, max_length=200, verbose_name='رابط الزر')),
                ('order', models.IntegerField(default=0, verbose_name='الترتيب')),
                ('is_active', models.BooleanField(default=True, verbose_name='نشط')),
            ],
            options={
                'verbose_name': 'شريحة عرض',
                'verbose_name_plural': 'شرائح العرض',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الاسم')),
                ('position', models.CharField(max_length=100, verbose_name='المنصب')),
                ('bio', models.TextField(verbose_name='نبذة مختصرة')),
                ('image', models.ImageField(upload_to='team/', verbose_name='الصورة')),
                ('is_board_member', models.BooleanField(default=False, verbose_name='عضو مجلس إدارة')),
                ('order', models.IntegerField(default=0, verbose_name='الترتيب')),
            ],
            options={
                'verbose_name': 'عضو الفريق',
                'verbose_name_plural': 'أعضاء الفريق',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الاسم')),
                ('position', models.CharField(max_length=100, verbose_name='المنصب')),
                ('company', models.CharField(max_length=100, verbose_name='الشركة')),
                ('testimonial', models.TextField(verbose_name='الشهادة')),
                ('image', models.ImageField(blank=True, upload_to='testimonials/', verbose_name='الصورة')),
                ('is_active', models.BooleanField(default=True, verbose_name='نشط')),
            ],
            options={
                'verbose_name': 'رأي عميل',
                'verbose_name_plural': 'آراء العملاء',
            },
        ),
    ]
