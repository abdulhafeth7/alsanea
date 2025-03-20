from django.contrib import admin
from .models import ServiceCategory, Service, ServiceImage, Project, ProjectImage

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order']
    list_filter = ['category', 'featured']
    search_fields = ['title', 'short_description', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order', 'featured']
    inlines = [ServiceImageInline]

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'location', 'status', 'start_date', 'featured']
    list_filter = ['status', 'featured', 'start_date']
    search_fields = ['title', 'client', 'location', 'short_description', 'description']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['services']
    list_editable = ['featured']
    inlines = [ProjectImageInline]
