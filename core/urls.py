from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path(_('about/'), views.about, name='about'),
    path(_('contact/'), views.contact, name='contact'),
    path(_('team/'), views.team, name='team'),
    path(_('partners/'), views.partners, name='partners'),
] 