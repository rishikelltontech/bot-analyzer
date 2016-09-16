from django.conf.urls import url
from  . import views
from django.views.static import serve as staticserve
from django.conf import settings

# if settings.DEBUG:
#     urlpatterns += patterns('',
#         (r'^static/(?P<path>.*)$', staticserve,
#             {'document_root': os.path.join(os.path.dirname(__file__), 'static')} ),
#         )
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.logins, name = 'login'),
	url(r'^logout/$', views.logouts, name='logout'),
	
]
