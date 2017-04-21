from django.contrib import admin

# Register your models here.
from . models import Type_of_animal,Sex,Pet,Photo,Ad

admin.site.register(Type_of_animal)
admin.site.register(Sex)
admin.site.register(Pet)
admin.site.register(Photo)
admin.site.register(Ad)