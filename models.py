from django.db import models
from django.utils import timezone
import uuid
from django.core.validators import MinLengthValidator, RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .validators import *


class Student(models.Model):
	StudentName = models.CharField(max_length = 20, blank = False, null = False)
	Regno = models.CharField(primary_key = True, max_length = 10, blank = False, null = False)
	BRANCHES = (
		('cse', 'ComputerScience'),
		('mech', 'MechanicalEngineering'),
		('ece', 'ElectronicsAndCommunication')	
	)
	EmailId = models.EmailField(unique = True)
	Password = models.CharField(max_length = 25, validators = [MinLengthValidator(8)])
	BranchName = models.CharField(max_length = 10 , blank = False, null = False,  choices = BRANCHES)

	def __str__(self):
		return self.Regno + "_cse"

@receiver(post_save, sender=Student)
def save_student(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(username=instance.EmailId, email=instance.EmailId, password=instance.Password)
        user.profile.type = 'u'
    user.save()

@receiver(post_delete, sender=Student)
def delete_student(sender, instance, **kwargs):
	User.objects.filter(username=instance.EmailId).delete()

class Admin(models.Model):
	EmailId = models.CharField(max_length = 20, blank = False, null = False)
	Password = models.CharField(max_length = 20, validators = [MinLengthValidator(8)])

@receiver(post_save, sender=Admin)
def save_admin(sender, instance, created, **kwargs):
    if created:
		#after this line, creater_user_profile method will be called
        user = User.objects.create_user(username=instance.EmailId, email=instance.EmailId, password=instance.Password)
        user.profile.type = 'a'
    user.save()

@receiver(post_delete, sender=Admin)
def delete_student(sender, instance, **kwargs):
	User.objects.filter(username=instance.EmailId).delete()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(default='u', max_length=1)

    def __str__(self):
        return self.user.username + " " + self.type

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class FeesNotification(models.Model):
	StartDate = models.DateField()
	EndDate = models.DateField()
	Description = models.CharField(max_length = 1000, blank = False, null = False)
	CHOICES = (
		('true', 'true'),
		('false', 'false')
	)
	HallTicketAvailable = models.CharField(choices = CHOICES, default = 'false', max_length = 5, validators = [MinLengthValidator(4)])


class FeesApplication(models.Model):
	StudentId = models.ForeignKey('Student', null = False, blank = False)
	SEMESTER = (
		('1', '1'),
		('2', '2'),
		('3', '3'),	
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8')
	)
	SemesterNo = models.CharField(choices = SEMESTER, max_length = 1, default = 'first')
	DebitCardNo = models.CharField(max_length = 12, default = '123456789111' ,validators = [MinLengthValidator(12)] )
	Cvv = models.CharField(max_length = 3, default = '123', validators =  [ MinLengthValidator(3) ])
	PaidFees = models.IntegerField(blank = False, null = False, default = 1890)

class FeesPayment(models.Model):
	ApplicationId = models.ForeignKey('FeesNotification', null = False, blank = False)
	StudentId = models.ForeignKey('Student', null = False, blank = False)
	PaidFees = models.IntegerField(null = False, blank = False)
	class Meta:
		unique_together = (("ApplicationId", "StudentId"), )