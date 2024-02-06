from django.db import models


from django.apps import apps

app_label = __package__.lower() if '.' not in __package__ else __package__.rsplit('.', 1)[-1].lower()

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        app_label = app_label

