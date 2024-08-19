from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    link = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.summary