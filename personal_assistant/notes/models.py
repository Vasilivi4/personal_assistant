from django.db import models

# Create your models here.
#classes for notes and tags. Each note might have multiple tags
class Note(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', blank=True)
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name