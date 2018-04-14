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
