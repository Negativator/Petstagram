from django.db import models


# Create your models here.
class Pet(models.Model):
    type = models.CharField(max_length=6, blank=False,
                            choices=[
                                ('cat', 'cat'),
                                ('dog', 'dog'),
                                ('parrot', 'parrot'),
                            ])
    name = models.CharField(max_length=6, blank=False)
    age = models.PositiveBigIntegerField()
    description = models.TextField(max_length=255)
    image_url = models.URLField(max_length=100,default='https://bitsofco.de/content/images/2018/12/broken-1.png')


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

