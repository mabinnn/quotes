from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'process$', views.register_logic),
    url(r'success$', views.success_logic),
    url(r'userlogin$', views.verify_logic),
    url(r'logout$', views.logout),
    url(r'contribute$', views.contribute_logic),
    # url(r'post$', views.post_logic),
    url(r'addlist/(?P<id>\d+)$', views.add_favorites)
]
