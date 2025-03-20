#!/bin/bash
# تثبيت متطلبات Python باستخدام خيارات إضافية لتجنب بناء العجلات المشكلة
pip install --no-build-isolation --upgrade pip
pip install --no-build-isolation -r requirements.txt

# تنفيذ هجرات قاعدة البيانات
python manage.py migrate

# جمع الملفات الثابتة
python manage.py collectstatic --no-input
