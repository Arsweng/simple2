from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 50,null = False, blank = False, unique = True)
    author = models.CharField(max_length = 100,null = False, blank = False)
    description = models.TextField(null = False, blank = False)
    price = models.FloatField(null = False, blank = False)
    pub_date = models.DateField()
    banner = models.ImageField(default = 'default.jpg', null = True, blank = True)
    def __str__(self):
        return self.title