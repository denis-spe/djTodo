from django.db import models
from django.utils import timezone

class ActivatyChoices(models.TextChoices):
    TASK = "TK", "Task"
    HABIT = "HT", "Habit"

# Create your models here.
class Activaties(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=260, default="")
    is_activate_done = models.BooleanField(default=False)
    activate_type = models.CharField(max_length=6, choices=ActivatyChoices)
    published_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s" % self.title