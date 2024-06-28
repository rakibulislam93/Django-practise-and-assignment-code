from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from musician.models import musicianModel
# Create your models here.

class albumModel(models.Model):
    album_name = models.CharField(max_length=100)
    album_relase_date = models.DateTimeField(auto_now_add=True)
    album_rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    musician = models.ForeignKey(musicianModel,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.album_name