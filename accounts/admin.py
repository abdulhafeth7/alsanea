from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'user__email', 'phone')
    list_filter = ('user__is_active', 'user__is_staff')
    raw_id_fields = ('user',)
