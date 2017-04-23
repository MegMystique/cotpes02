from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Pet,Photo,Ad
from django.template import loader
from django.views import generic
from django.http import Http404
#

# def index(request):
#     all_pet_list = Pet.objects.all()
#     print(all_pet_list)
#     template = loader.get_template('find_cat/index.html')
#     context = {
#         'all_pet_list': all_pet_list,
#     }
#     return HttpResponse(template.render(context, request))
class BaseIndexView(generic.TemplateView):
    template_name = 'find_cat/base_generic.html'
class IndexView(generic.ListView):
    template_name = 'find_cat/index.html'
    context_object_name = 'all_ad_list'

    def get_queryset(self):
        """Return the all pets published questions."""
        return Ad.objects.order_by('was_published')[:3]
# class DetailView(generic.DetailView):
#     model = Pet
#     template_name = 'find_cat/detail.html'
def detail(request, pet_id):#need change it by class-based

    try:
        pet = Pet.objects.get(pk=pet_id)
        all_photo_pet=Photo.objects.all().filter(pet=pet)
        print(all_photo_pet)
    except Pet.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'find_cat/detail.html', {'pet': pet,'all_photo_pet': all_photo_pet})