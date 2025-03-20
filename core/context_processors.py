from core.models import SiteSettings

def site_settings(request):
    """
    إضافة إعدادات الموقع إلى سياق القوالب
    """
    try:
        settings = SiteSettings.objects.first()
        if not settings:
            settings = None
    except Exception:
        settings = None
        
    return {
        'site_settings': settings
    } 