# دليل نشر موقع الصانع على PythonAnywhere

هذا الدليل يشرح خطوات نشر موقع Django الخاص بشركة الصانع على استضافة PythonAnywhere المجانية.

## 1. تسجيل حساب على PythonAnywhere

1. قم بزيارة [موقع PythonAnywhere](https://www.pythonanywhere.com) وإنشاء حساب مجاني.
2. بعد التسجيل، سيكون لديك اسم مستخدم سيصبح جزءًا من عنوان موقعك (`yourusername.pythonanywhere.com`).

## 2. تحضير الملفات للنشر

تأكد من أن مشروعك يحتوي على الملفات التالية:

- `requirements.txt` - يحتوي على جميع المكتبات اللازمة للمشروع
- `.env.production` - ملف الإعدادات لبيئة الإنتاج
- `pythonanywhere_wsgi.py` - ملف مرجعي لإعداد WSGI على PythonAnywhere

## 3. رفع الملفات إلى PythonAnywhere

### باستخدام Git (الطريقة المفضلة):

1. انتقل إلى علامة التبويب "Consoles" وافتح وحدة طرفية Bash جديدة.
2. قم بنسخ المستودع من GitHub (إذا كان موجودًا):
   ```bash
   git clone https://github.com/yourusername/alsanea.git
   ```

### باستخدام رفع الملفات يدويًا:

1. في PythonAnywhere، انتقل إلى علامة التبويب "Files".
2. قم بإنشاء مجلد جديد باسم "alsanea".
3. انتقل إلى هذا المجلد وارفع ملفات المشروع باستخدام زر "Upload".

## 4. إعداد البيئة الافتراضية

1. انتقل إلى علامة التبويب "Consoles" وافتح وحدة طرفية Bash جديدة.
2. قم بإنشاء بيئة افتراضية:
   ```bash
   mkvirtualenv --python=python3.9 alsanea-venv
   ```
3. تفعيل البيئة الافتراضية:
   ```bash
   workon alsanea-venv
   ```
4. انتقل إلى مجلد المشروع:
   ```bash
   cd ~/alsanea
   ```
5. تثبيت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```

## 5. تعديل ملفات الإعدادات

1. انسخ ملف .env.production إلى .env:
   ```bash
   cp .env.production .env
   ```
2. عدل ملف .env:
   ```bash
   nano .env
   ```
3. قم بتحديث ALLOWED_HOSTS لتشمل اسم موقعك على PythonAnywhere:
   ```
   ALLOWED_HOSTS=yourusername.pythonanywhere.com
   ```
4. قم بتوليد مفتاح SECRET_KEY جديد وآمن:
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```
   ثم انسخ المفتاح الناتج إلى ملف .env.

## 6. إعداد قاعدة البيانات

1. في وحدة طرفية Bash، قم بتشغيل الهجرات:
   ```bash
   python manage.py migrate
   ```
2. إنشاء مستخدم مسؤول:
   ```bash
   python manage.py createsuperuser
   ```
3. جمع الملفات الثابتة:
   ```bash
   python manage.py collectstatic --no-input
   ```

## 7. إعداد تطبيق الويب

1. انتقل إلى علامة التبويب "Web".
2. انقر على "Add a new web app".
3. اختر "Manual configuration".
4. اختر "Python 3.9" (أو الإصدار المتوافق مع مشروعك).

### إعداد البيئة الافتراضية:

1. في قسم "Virtualenv"، أدخل مسار البيئة الافتراضية:
   ```
   /home/yourusername/.virtualenvs/alsanea-venv
   ```

### إعداد ملف WSGI:

1. انقر على رابط ملف WSGI وسيفتح في محرر النصوص.
2. احذف كل المحتوى واستبدله بمحتوى من ملف `pythonanywhere_wsgi.py` (مع تعديل المسارات وفقًا لاسم المستخدم الخاص بك).

### إعداد المجلدات الثابتة:

1. في قسم "Static files"، أضف المسارات التالية:
   - URL: `/static/`، Directory: `/home/yourusername/alsanea/staticfiles`
   - URL: `/media/`، Directory: `/home/yourusername/alsanea/media`

## 8. إعادة تشغيل التطبيق

1. انقر على زر "Reload" الأخضر.
2. انتظر لحظات حتى يتم إعادة تشغيل التطبيق.
3. انتقل إلى `yourusername.pythonanywhere.com` للتحقق من أن موقعك يعمل بشكل صحيح.

## ملاحظات إضافية

- **للتحديثات المستقبلية**: عند إجراء تغييرات على الكود، قم بسحب التحديثات باستخدام Git (إذا كنت تستخدمه)، ثم شغّل الهجرات وجمع الملفات الثابتة مرة أخرى إذا لزم الأمر، وأخيرًا اضغط على "Reload".
- **للصيانة**: يتيح لك الحساب المجاني على PythonAnywhere تشغيل تطبيق واحد فقط، ويجب عليك زيارة لوحة التحكم مرة كل ثلاثة أشهر لتجنب إيقاف التطبيق.
- **حدود الاستضافة المجانية**: يوفر الحساب المجاني على PythonAnywhere مساحة تخزين محدودة ومعالجة محدودة وعرض نطاق محدود، لذا تأكد من تحسين موقعك للعمل ضمن هذه القيود.
