from django.contrib import admin
from .models import Student, Profile,Admin, FeesNotification, FeesApplication, FeesPayment
# Register your models here.
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Admin)
admin.site.register(FeesNotification)
admin.site.register(FeesApplication)
admin.site.register(FeesPayment)
