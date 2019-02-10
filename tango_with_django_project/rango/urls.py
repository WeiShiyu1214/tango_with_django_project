from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^about',views.about,name='about'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_pages/$', views.add_page, name='add_page'),
	url(r'goto/$', views.track_url, name='goto'),
]