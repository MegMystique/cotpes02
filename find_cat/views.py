from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Pet,Photo
from django.template import loader
from django.views import generic
from django.http import Http404
#
def index(request):
    all_pet_list = Pet.objects.all()
    print(all_pet_list)
    template = loader.get_template('find_cat/index.html')
    context = {
        'all_pet_list': all_pet_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, pet_id):

    try:
        pet = Pet.objects.get(pk=pet_id)
        all_photo_pet=Photo.objects.all().filter(pet=pet)
        print(all_photo_pet)
    except Pet.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'find_cat/detail.html', {'pet': pet,'all_photo_pet': all_photo_pet})