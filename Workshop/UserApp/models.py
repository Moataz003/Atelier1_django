from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError
from ConferenceApp.models import Submission
from django.core.validators import RegexValidator
import uuid
def generate_userid():
    return "USER"+uuid.uuid4().hex[:4].upper()

def verify_email(email):
   domaine=["esprit.tn","seasame.com","tekup.tn","central.com"]
   if email.split("@")[1] not in domaine:
       raise ValidationError("l'email est invalide et doit appartenir a un domaine universitaire")
   

name_validator = RegexValidator(
    regex=r'^[A-Za-z\s-]+$',
    message="ce champs doit avoir des lettre et des espaces"
)


class User(AbstractUser):
    User_id=models.CharField(max_length=8,primary_key=True,unique=True,editable=False)
    first_name=models.CharField(max_length=15,validators=[name_validator])
    last_name=models.CharField(max_length=15,validators=[name_validator])
    email=models.CharField(max_length=50,unique=True,validators=[verify_email])
    affiliation=models.CharField(max_length=255)
    nationality=models.CharField(max_length=255)

    Role=[
        ("participant","participant"),
        ("comitee","organizing comitee member")
    ]
    role=models.CharField(max_length=255,choices=Role)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        if not self.User_id:
            new_id=generate_userid()
            while User.objects.filter(User_id=new_id).exists():
                new_id=generate_userid()
            self.User_id=new_id
        super().save(*args,**kwargs)
    #submissions=models.ManyToManyField("ConfernceApp.Conference",through=Submission)
   # OrginizingComittee=models.ManyToManyField("ConfernceApp.Conference",through=OrginizingComittee)


class OrginizingComittee(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="commitee")
    conference_id=models.ForeignKey("ConferenceApp.Conference",on_delete=models.CASCADE,related_name="commitee")

    Choices=[("chair","chair"),
         ("member","member")
         
         ]
    comitte_role=models.CharField(max_length=255,choices=Choices)
    date_joined=models.DateTimeField(auto_now_add=True)

