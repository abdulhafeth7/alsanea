# تعليمات نقل الصور في مجلد الصور

بناءً على دليل الصور السابق، يجب تنظيم الصور الحالية من خلال نقلها إلى المجلدات المناسبة التي تم إنشاؤها. هذه التعليمات توضح كيفية نقل الصور بالخطوات.

## الخطوات المطلوبة

1. افتح موجه أوامر ويندوز (cmd) أو Windows PowerShell.
2. انتقل إلى مجلد المشروع:
   ```
   cd D:\Alsanea
   ```

3. نقل صور المشاريع:
   ```
   mkdir -Force static\images\projects
   copy static\images\alsanea (1).jpg static\images\projects\
   copy static\images\alsanea (2).jpg static\images\projects\
   copy static\images\alsanea (3).jpg static\images\projects\
   copy static\images\alsanea (4).jpg static\images\projects\
   copy static\images\project (1).jpg static\images\projects\
   copy static\images\project (2).jpg static\images\projects\
   copy static\images\project (3).jpg static\images\projects\
   ```

4. نقل صور الخدمات:
   ```
   mkdir -Force static\images\services
   copy static\images\alsanea (5).jpg static\images\services\
   copy static\images\alsanea (6).jpg static\images\services\
   copy static\images\alsanea (7).jpg static\images\services\
   ```

5. نقل صور الخلفيات:
   ```
   mkdir -Force static\images\backgrounds
   copy static\images\alsanea (12).jpg static\images\backgrounds\
   ```

6. نقل صور فريق العمل:
   ```
   mkdir -Force static\images\team
   copy static\images\engineer (1).webp static\images\team\team1.webp
   copy static\images\engineer (2).webp static\images\team\team2.webp
   copy static\images\engineer (3).webp static\images\team\team3.webp
   ```

7. إنشاء مجلد الأنماط:
   ```
   mkdir -Force static\images\patterns
   ```

8. إنشاء مجلد الشهادات:
   ```
   mkdir -Force static\images\certificates
   ```

## إنشاء صورة النمط Pattern.png

1. افتح ملف `static/images/patterns/pattern_creator.html` في متصفح الإنترنت.
2. انقر على زر "إنشاء النمط" لتوليد النمط.
3. انقر على زر "حفظ الصورة" لتنزيل الصورة كملف PNG.
4. انقل الصورة المحفوظة إلى مجلد `static/images/patterns` وأعد تسميتها إلى `pattern.png`.

## ملاحظات هامة

1. لا تحذف الصور الأصلية من المجلد الرئيسي إلا بعد التأكد من عملها في المجلدات الجديدة.
2. تأكد من تحديث مسارات الصور في ملفات HTML بعد نقل الصور.
3. استخدم أداة تحسين الصور لتقليل حجم الصور قبل استخدامها إذا كانت كبيرة (مثل الصورة `alsanea (10).jpg` التي حجمها 1.2 ميجابايت). 