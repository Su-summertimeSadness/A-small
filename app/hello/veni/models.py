from django.db import models


# Create your models here.

class Name(models.Model):

    data = models.JSONField()

    def __str__(self):
        return str(self.data)

    def obj_to_dict(self):
        return {
            'data': self.data
        }
