#!/usr/bin/env python
"""
سكريبت للتحقق من جاهزية البيئة المحلية للنشر على بيئة الإنتاج
"""
import os
import sys
import re
import subprocess
from pathlib import Path

# تحقق من وجود Python 3
print("تحقق من إصدار Python...")
python_version = sys.version_info
if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
    print("⚠️ تحذير: يُوصى باستخدام Python 3.8 أو أحدث. إصدارك الحالي هو {}.{}.{}".format(
        python_version.major, python_version.minor, python_version.micro))
else:
    print("✅ Python {}.{}.{} متوافق".format(
        python_version.major, python_version.minor, python_version.micro))

# تحقق من وجود ملف requirements.txt
print("\nتحقق من ملف requirements.txt...")
if os.path.isfile("requirements.txt"):
    print("✅ ملف requirements.txt موجود")
    
    # تحقق من المكتبات المثبتة
    try:
        installed_packages = subprocess.check_output([sys.executable, "-m", "pip", "freeze"], text=True)
        with open("requirements.txt", "r") as f:
            requirements = f.read()
        
        required_packages = [pkg.split('==')[0].lower() for pkg in requirements.splitlines() if pkg and not pkg.startswith('#')]
        installed_packages = [pkg.split('==')[0].lower() for pkg in installed_packages.splitlines() if pkg]
        
        missing_packages = []
        for pkg in required_packages:
            if pkg and pkg not in installed_packages:
                missing_packages.append(pkg)
        
        if missing_packages:
            print("⚠️ تحذير: المكتبات التالية غير مثبتة:")
            for pkg in missing_packages:
                print("  - {}".format(pkg))
            print("قم بتثبيت المكتبات المفقودة باستخدام: pip install -r requirements.txt")
        else:
            print("✅ جميع المكتبات المطلوبة مثبتة")
    except Exception as e:
        print("⚠️ حدثت مشكلة أثناء التحقق من المكتبات المثبتة:", str(e))
else:
    print("❌ ملف requirements.txt غير موجود")
    print("قم بإنشاء الملف باستخدام: pip freeze > requirements.txt")

# تحقق من ملفات الإعدادات
print("\nتحقق من ملفات الإعدادات...")
project_dirs = [d for d in os.listdir() if os.path.isdir(d) and not d.startswith('.') and not d == 'venv']
settings_files = []

for d in project_dirs:
    settings_path = os.path.join(d, "settings.py")
    if os.path.isfile(settings_path):
        settings_files.append(settings_path)

if not settings_files:
    print("⚠️ لم يتم العثور على ملف settings.py")
else:
    for settings_file in settings_files:
        print(f"فحص {settings_file}...")
        with open(settings_file, "r") as f:
            content = f.read()
            
            # تحقق من DEBUG
            debug_match = re.search(r'DEBUG\s*=\s*([^#\n]+)', content)
            if debug_match:
                debug_value = debug_match.group(1).strip()
                if 'True' in debug_value and 'config' not in debug_value.lower():
                    print("⚠️ تحذير: وضع التطوير DEBUG مفعّل في {}".format(settings_file))
                    print("   قم بتغييره إلى DEBUG = False في بيئة الإنتاج")
                else:
                    print("✅ إعداد DEBUG صحيح")
            
            # تحقق من ALLOWED_HOSTS
            hosts_match = re.search(r'ALLOWED_HOSTS\s*=\s*([^#\n]+)', content)
            if hosts_match:
                hosts_value = hosts_match.group(1).strip()
                if '[]' in hosts_value and 'config' not in hosts_value.lower():
                    print("⚠️ تحذير: ALLOWED_HOSTS فارغ في {}".format(settings_file))
                    print("   قم بإضافة اسم موقعك إلى ALLOWED_HOSTS")
                else:
                    print("✅ إعداد ALLOWED_HOSTS يبدو صحيحًا")
            
            # تحقق من SECRET_KEY
            if "SECRET_KEY" in content and "config" not in content.lower():
                print("⚠️ تحذير: يجب استخدام متغير بيئي لـ SECRET_KEY بدلًا من كتابته مباشرة في الكود")

# تحقق من ملف .env.production
print("\nتحقق من ملف .env.production...")
if os.path.isfile(".env.production"):
    print("✅ ملف .env.production موجود")
else:
    print("❌ ملف .env.production غير موجود")
    print("قم بإنشاء ملف .env.production للإعدادات المخصصة لبيئة الإنتاج")

# تحقق من collectstatic
print("\nتحقق من الملفات الثابتة...")
if os.path.isdir("staticfiles"):
    print("✅ مجلد staticfiles موجود")
else:
    print("⚠️ تحذير: مجلد staticfiles غير موجود")
    print("قم بتشغيل الأمر: python manage.py collectstatic")

# تحقق من وجود ملف WSGI لـ PythonAnywhere
print("\nتحقق من ملف WSGI...")
if os.path.isfile("pythonanywhere_wsgi.py"):
    print("✅ ملف pythonanywhere_wsgi.py موجود")
else:
    print("❌ ملف pythonanywhere_wsgi.py غير موجود")
    print("قم بإنشاء ملف WSGI مخصص للاستضافة على PythonAnywhere")

print("\nتم الانتهاء من فحص جاهزية النشر. قم بمعالجة أي تحذيرات أو أخطاء قبل النشر على بيئة الإنتاج.") 