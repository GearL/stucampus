from django.conf.urls import url, patterns

from stucampus.magazine.views import magazine_list, display, manage
from stucampus.magazine.views import ModifyView, AddView, delete


urlpatterns = patterns(
    '',
    url(r'^upload/$', AddView.as_view(), name='add'),
    url(r'^manage/$', manage, name='manage'),
    url(r'^modify/$', ModifyView.as_view(), name='modify'),
    url(r'^delete/$', delete, name='delete'),

    # this two url should be placed after other urls
    # without regex ,in case they will disable other url
    url(r'^(?P<name>\D*)/$', magazine_list, name='list'),
    url(r'^display/(?P<id>\d)/$', display, name='display'),
)
