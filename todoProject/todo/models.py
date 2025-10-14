from django.db import models

# Create your models here.
class Activities(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=260)
    published_time = models.DateTimeField()

    def __str__(self):
        return "%s" % self.title