from django.db import models

# Create your models here.


LANGUAGES_CHOICES={
    ("EN","ENGLISH"),
    ("CS","CASTELLANO"),
    ("FR","FRENCH"),
}


class torrent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to="torrents")
    language = models.CharField(choices=LANGUAGES_CHOICES,max_length=2)
    date = models.DateField()
    torrent_file = models.FileField(unique=True, null=True,upload_to='torrents')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    


