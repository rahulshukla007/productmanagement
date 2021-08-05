from django.db import models
import datetime
import os

# Create your models here.
def filepath(request, filename):
    timenow = datetime.datetime.now().strftime("%m%d%Y%H:%M:%S")
    new_filename = f'{timenow}{filename}'
    return os.path.join('upload/', new_filename)



class Item(models.Model):
    product_name = models.TextField(max_length = 150)
    category = models.TextField(max_length = 150)
    description = models.TextField(max_length = 500, null=True)
    image = models.ImageField(upload_to = filepath, null=True, blank=True)