from django.db import models

# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=50)
    book_id = models.IntegerField(default=3)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    


    def __str__(self):
        return str(self.name)+" "+str(self.author)