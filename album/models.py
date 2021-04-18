from django.db import models

# Create your models here.
class Image(models.Model):
    picture_id = models.AutoField(primary_key=True)
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '料理画像'
        verbose_name_plural = '料理画像'
