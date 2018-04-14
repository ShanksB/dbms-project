from django.conf.urls import url
from . import views

from django.conf.urls.static import static

urlpatterns = [
 	url(r'^$', views.homepage, name = 'home_page' ),
 	url(r'^register/$', views.register_student, name = "register_student"),
	url(r'^login/$', views.login_student, name = "login_student"),
 	url(r'^dashboard/$', views.dashboard, name = "dashboard"),
 	url(r'^logout/$', views.logout_view, name = "logout"),
 		
 ]