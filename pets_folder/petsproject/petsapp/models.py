from django.db import models

# Create your models here.
class Pets(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
def __str__(self):
    return self.name