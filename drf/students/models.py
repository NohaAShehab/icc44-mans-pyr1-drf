from django.db import models

from tracks.models import Track
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    grade = models.IntegerField(default=0, null=True, blank=True)
    image =  models.ImageField(upload_to='students/images/', null=True, blank=True)
    track  = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True, related_name='students')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.name}"


    @classmethod
    def get_all_students(cls):
        return  cls.objects.all()