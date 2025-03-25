from django.db import models

# Songs Model

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=200)
    gerne = models.CharField(max_length=200)
    audio_url = models.CharField(max_length=300)
    duration = models.CharField(max_length=20)
    cover_image = models.ImageField(upload_to='cover_image/',blank=True,null=True)
    
    def __str__(self):
        return self.title