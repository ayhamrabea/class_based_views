from django.db import models
from django.utils import timezone

class Post(models.Model):

    titil = models.CharField( max_length=50)
    content = models.TextField()
    time_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField( upload_to='post_img')

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.titil

