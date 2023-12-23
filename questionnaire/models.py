from django.db import models
from django.contrib.auth.models import User

# Create your models here.

YES_OR_NO = [("Yes", "Yes"), ("No", "No")]
GENDER = [("Male", "Male"), ("Female", "Female"), ("Unknown", "Unknown")]

class Questionnaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=25, null=True, blank=True)
    disability = models.CharField(choices=YES_OR_NO, max_length=3, null=False, blank=False)
    previous_experience = models.CharField(choices=YES_OR_NO, max_length=3 null=False, blank=False)
    previous_training = models.CharField(choices=YES_OR_NO, null=False, blank=False)
    physicians_name = models.CharField(max_length=75, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)