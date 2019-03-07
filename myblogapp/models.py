from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.TextField(null=True)
    body = models.TextField()

    def summary(self):
        if len(self.body) > 100: return self.body[:100] + '...'
        else: return self.body

    def is_authorized(self):
        if self.author == '' or self.author == '-1': return "Anonymous"
        else: return self.author