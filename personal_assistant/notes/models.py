from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# classes for notes and tags. Each note might have multiple tags
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]
    def __str__(self):
        return self.name
