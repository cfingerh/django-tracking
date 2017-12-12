try:
    from django.urls import re_path
except ImportError:
    from django.conf.urls import url as re_path
from django.conf import settings
from tracking import views

urlpatterns = (
    re_path(r'^refresh/$', views.update_active_users, name='tracking-refresh-active-users'),
    re_path(r'^refresh/json/$', views.get_active_users, name='tracking-get-active-users'),
)

if getattr(settings, 'TRACKING_USE_GEOIP', False):
    urlpatterns += (
        re_path(r'^map/$', views.display_map, name='tracking-visitor-map'),
    )
