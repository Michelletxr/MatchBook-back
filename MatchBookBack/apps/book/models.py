from django.db import models
from MatchBookBack.abstracts.base_models import BaseModel
from django.utils.translation import gettext_lazy as _
#from authentication.models import User
# Create your models here.

class Book(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Nome'))
    author = models.CharField(max_length=255, verbose_name=_('Autor'))
   # user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: 
        app_label = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return self.name
    


