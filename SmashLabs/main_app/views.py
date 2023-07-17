from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Fighter

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def fighters_index(request):
   return render(request, 'fighters/index.html', {
      'fighters': Fighter.objects.all()
   }) 

def fighters_detail(request, fighter_id):
   fighter = Fighter.objects.get(id=fighter_id)
   return render(request, 'fighters/detail.html', {'fighter': fighter})