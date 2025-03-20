from django.contrib import admin
from .models import UserActionLog

@admin.register(UserActionLog)
class UserActionLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action_type', 'model_name', 'timestamp', 'ip_address']
    list_filter = ['action_type', 'timestamp', 'user']
    search_fields = ['user__username', 'description', 'model_name']
    readonly_fields = ['user', 'action_type', 'model_name', 'object_id', 'description', 'timestamp', 'ip_address']
