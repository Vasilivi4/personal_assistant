from django.db import models

# Create your models here.

class Notes(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title