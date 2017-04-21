from django.db import models

# Create your models here.
class Type_of_animal(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Sex(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Pet(models.Model):
    type_animal=models.ForeignKey(Type_of_animal)
    name=models.CharField(max_length=100)
    sex=models.ForeignKey(Sex)
    age=models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    sterilized=models.BooleanField(blank=True)
    accustomed=models.BooleanField(blank=True)
    #photo = models.ForeignKey(Photo,on_delete=models.CASCADE)
    get_home = models.BooleanField()
    def __str__(self):
        return str(self.type_animal)+ " "+str(self.name)+" "+str(self.age)
class Photo(models.Model):
    photo = models.ImageField(upload_to='find_cat/static/find_cat/img/',blank=True)
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE)
    def __str__(self):
        print(self.photo.url)
        x=str(self.photo.url).find('img/')
        print(x)
        return self.photo.url[x+4:]
class Ad(models.Model):
    pet=models.ForeignKey(Pet)
    comment=models.TextField(max_length=300)
    was_published=models.DateTimeField()
    phone=models.CharField(max_length=100)
    def __str__(self):
        return str(self.pet)
