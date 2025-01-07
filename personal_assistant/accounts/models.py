from django.db import models
from django.contrib.auth.models import User
# from PIL import Image
# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(default='default_image.png', upload_to='profile_images')
#
#     def __str__(self):
#         return self.user.username
#
#     def save(self, *args, **kwargs):
#         super().save()
#
#         img = Image.open(self.avatar.path)
#
#         if img.height > 250 or img.width > 250:
#             new_img = (250, 250)
#             img.thumbnail(new_img)
#             img.save(self.avatar.path)