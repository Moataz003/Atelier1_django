from ast import Import
from django.db import models
from django.core.validators import MinLengthValidator 
from django.core.exceptions import ValidationError

# Create your models here.
class Conference(models.Model):
    conference_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255,validators=[MinLengthValidator(30,"la description doit contenir au moins 3 caractere")])
    
    THEME = [
        ("CS&IA","Computer Science and IA"),
        ("SE","Science and eng")
    ]
    
    theme=models.CharField(max_length=255,choices=THEME)
    start_date=models.DateField()
    end_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def clean(self):
        if self.start_date > self.end_date :
           raise ValidationError("la date de fin doit etre sup a la date de debut")
    



class Submission(models.Model):
    submission_id=models.CharField(primary_key=True,max_length=255,unique=True)
    user=models.ForeignKey("UserApp.User",on_delete=models.CASCADE,related_name="submissions")
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name="submissions")
    title=models.CharField(max_length=255)
    abstract=models.TextField()
    keywords=models.TextField()
    paper=models.FileField(upload_to="papers/")
    Choises=[("submitted","submitted"),
        ("under review","under reveiw"),
        ("accepted","accepted"),
        ("rejected","rejected")]

    status=models.CharField(max_length=255,choices=Choises)
    submission_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
