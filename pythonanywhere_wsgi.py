"""
ملف WSGI المخصص لاستضافة موقع Django على PythonAnywhere
استخدم هذا الملف كمرجع عند إعداد تطبيق الويب على PythonAnywhere
"""

import os
import sys

# إضافة مسار المشروع إلى المسارات المتاحة
path = '/home/yourusername/alsanea'  # غير هذا المسار حسب اسم المستخدم الخاص بك على PythonAnywhere
if path not in sys.path:
    sys.path.append(path)

# تعيين متغيرات البيئة للإعدادات
os.environ['DJANGO_SETTINGS_MODULE'] = 'alsanea.settings'

# تفعيل البيئة الافتراضية إذا كنت تستخدمها
# activate_this = '/home/yourusername/.virtualenvs/myenv/bin/activate_this.py'
# with open(activate_this) as file_:
#     exec(file_.read(), dict(__file__=activate_this))

# استيراد تطبيق WSGI من Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 