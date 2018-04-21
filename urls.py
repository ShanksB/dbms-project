from django.conf.urls import url
from . import views

from django.conf.urls.static import static

urlpatterns = [
 	url(r'^$', views.homepage, name = 'home_page' ),
 	url(r'^register/$', views.register_student, name = "register_student"),
	url(r'^login/$', views.login_student, name = "login_student"),
 	url(r'^dashboard/$', views.dashboard, name = "dashboard"),
	url(r'^dashboard/pay/$', views.pay_fees, name = "pay_fees"),
 	url(r'^logout/$', views.logout_view, name = "logout"),
 	url(r'^download_ht/$', views.download_hall_ticket, name = "download_hall_ticket"),

	 # admin urls
	url(r'^login_a/$', views.login_admin, name = "login_admin"),
 	url(r'^dashboard_a/$', views.dashboard_admin, name = "dashboard_admin"),
	url(r'^open_fees_application/$', views.open_fees_application, name = "open_fees_application"),
	url(r'^extend_fees_date/$', views.extend_fees_date, name = "extends_fees_date"),
	url(r'^send_fees_reminder/$', views.send_fees_reminder, name = "send_fees_reminder"),
 	url(r'^close_fees_application/$', views.close_fees_application, name = "close_fees_application"),
	url(r'^hall_ticket_printout/$',views.hall_ticket_printout, name = "hall_ticket_printout"),


	
 		
 ]