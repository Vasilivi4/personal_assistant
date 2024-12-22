from django.db import models
from django.contrib.auth.models import User

class NewsSummary(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_summaries', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
