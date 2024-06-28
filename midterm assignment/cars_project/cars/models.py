from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BrandModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,null=True ,blank=True)
     
    def __str__(self) -> str:
        return self.name
    

class CarModel(models.Model):
    brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='cars/media/uploads',blank=True,null=True)


    def __str__(self) -> str:
        return self.name
    

class CommentModel(models.Model):
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Comments by {self.name}'

class BuyCarModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username}'