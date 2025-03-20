# مشروع الصانع - Alsanea Project

موقع شركة الصانع المبني باستخدام Django Framework.

## المميزات

- موقع كامل ثنائي اللغة (العربية والإنجليزية)
- عرض خدمات الشركة ومشاريعها
- نظام إدارة محتوى متكامل
- تصميم متجاوب مع جميع الأجهزة
- لوحة تحكم للإدارة

## متطلبات النظام

- Python 3.8+
- PostgreSQL (أو SQLite للتطوير)
- Virtualenv (موصى به)

## التثبيت

1. استنساخ المشروع:
```
git clone [رابط المستودع]
cd alsanea_project
```

2. إنشاء بيئة افتراضية وتفعيلها:
```
python -m venv venv
# على Windows
venv\Scripts\activate
# على Linux/Mac
source venv/bin/activate
```

3. تثبيت المتطلبات:
```
pip install -r requirements.txt
```

4. إنشاء ملف `.env` في المجلد الرئيسي وإضافة المتغيرات البيئية:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3  # للتطوير فقط
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. تنفيذ الترحيلات:
```
python manage.py migrate
```

6. إنشاء مستخدم مسؤول:
```
python manage.py createsuperuser
```

7. تشغيل خادم التطوير:
```
python manage.py runserver
```

## الهيكل العام للمشروع

```
alsanea_project/
│
├── alsanea/                      # مشروع Django الرئيسي
├── core/                         # تطبيق جوهر الموقع
├── services/                     # تطبيق الخدمات والمشاريع
├── dashboard/                    # تطبيق لوحة التحكم للإدارة
├── locale/                       # ملفات الترجمة
├── static/                       # الملفات الثابتة
├── media/                        # ملفات الوسائط المتعددة
├── templates/                    # قوالب عامة
│
├── requirements.txt              # متطلبات المشروع
├── manage.py                     # سكريبت إدارة جانقو
├── .env                          # متغيرات البيئة
└── README.md                     # توثيق المشروع
```

## المساهمة

نرحب بالمساهمات! يرجى إنشاء فرع (branch) جديد وتقديم طلب سحب (pull request) للمراجعة.

## الترخيص

هذا المشروع مرخص بموجب [نوع الترخيص]. 