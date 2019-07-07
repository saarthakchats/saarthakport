from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    pubdate = models.DateTimeField()

    def __str__(self):
        return self.title

    def preview(self):
        return self.body[:100]
    def pretty_date(self):
        return self.pubdate.strftime('%b %e, %Y')
