from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path(_('content/'), views.content_manager, name='content_manager'),
    path(_('media/'), views.media_manager, name='media_manager'),
    path(_('users/'), views.users_manager, name='users_manager'),
    path(_('settings/'), views.settings, name='settings'),
] 