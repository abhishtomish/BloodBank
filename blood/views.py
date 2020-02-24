from django.shortcuts import render
from blood.models import Blood
# Create your views here.
def details(request):
    context = {}
    blood = Blood.objects.all()
    context['blood'] = blood
    return render(request, 'blood/details.html', context)