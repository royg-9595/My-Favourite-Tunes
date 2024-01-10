from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title