from microdjango.db import models

class Tag(models.Model):
    name = models.CharField(max_length=40)
    num = models.IntegerField()
