from django.db import models

# Create your models here.


class Track(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='tracks/logos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_objects(cls):
        return  cls.objects.all()


    @classmethod
    def get_specific_object(cls, id):
        return  cls.objects.filter(id=id).first()
