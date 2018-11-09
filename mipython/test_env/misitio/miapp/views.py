from django.shortcuts import render
from django.utils import timezone
from .models import Automovil

# Create your views here.
def post_list(request):
    posts = Automovil.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'miapp/post_list.html', {'posts': posts})
