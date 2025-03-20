#!/bin/bash
# تثبيت متطلبات Python
pip install -r requirements.txt

# تنفيذ هجرات قاعدة البيانات
python manage.py migrate

# جمع الملفات الثابتة
python manage.py collectstatic --no-input
