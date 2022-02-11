import email
from tabnanny import verbose
from django.db import models
from django.forms import ModelForm

# Create your models here.
class WebblogFormModel(models.Model):    

    topic = models.CharField(max_length=50)
    content = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    post_date = models.DateField()

    class Meta:
        verbose_name = 'WebblogFormModel'
        verbose_name_plural = 'WebblogFormModels'

    def __str__(self) -> str:
        return self.name


class WebblogForm(ModelForm):
    class Meta:
        model = WebblogFormModel
        fields = ('topic', 'content', 'name', 'email', 'post_date')

