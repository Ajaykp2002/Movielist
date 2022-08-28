from django.db import models

# Create your models here.
class movies(models.Model):
    Movie_Name=models.CharField(max_length=100)
    Movie_description=models.TextField()
    Movie_Year=models.IntegerField()
    Movie_img=models.ImageField(upload_to='pic')
    def __str__(self):
        return self.Movie_Name
