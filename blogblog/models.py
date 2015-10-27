from django.db import models

class Message(models.Model):
   title = models.CharField(max_length=100)
   date = models.DateField(blank=True, null=True)
   text = models.TextField(max_length=3000)
   
   def __str__(self):
      return self.title #, self.text, self.date
