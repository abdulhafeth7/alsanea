<<<<<<< HEAD
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
=======
# مشروع الصانع

<p align="center">
  <img src="static/images/logo.png" alt="شعار الصانع" width="200">
</p>

موقع شركة الصانع هو منصة إلكترونية تعرض خدمات ومشاريع الشركة في مجال المقاولات والبناء. يوفر الموقع واجهة سهلة الاستخدام للعملاء للتعرف على الشركة وخدماتها ومشاريعها السابقة، كما يتيح التواصل معها بسهولة.

## المميزات الرئيسية

- عرض المشاريع السابقة مع صور وتفاصيل
- قائمة الخدمات المقدمة مع وصف تفصيلي
- نبذة عن الشركة وفريق العمل
- صفحة تواصل مع نموذج للاستفسارات
- لوحة تحكم إدارية متكاملة
- واجهة متجاوبة مع جميع الأجهزة

## التقنيات المستخدمة

- **لغة البرمجة**: Python 3.9
- **إطار العمل**: Django 4.2
- **قاعدة البيانات**: SQLite (للتطوير)، PostgreSQL (للإنتاج)
- **واجهة المستخدم**: HTML5, CSS3, JavaScript
- **إطار CSS**: Bootstrap 5
- **معالجة الصور**: Pillow
- **الاستضافة**: Render

## متطلبات التشغيل

- Python 3.9 أو أحدث
- pip (مدير حزم Python)
- virtualenv (بيئة Python افتراضية)

## طريقة التثبيت

### 1. استنساخ المستودع

```bash
git clone https://github.com/YOUR_USERNAME/alsanea.git
cd alsanea
```

### 2. إنشاء بيئة افتراضية وتفعيلها

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. تثبيت المتطلبات

```bash
pip install -r requirements.txt
```

### 4. إعداد ملف البيئة

قم بإنشاء ملف `.env` في المجلد الرئيسي واضبط المتغيرات التالية:
>>>>>>> c133260ad71734a6512bcd223f5f5fec961ed810
