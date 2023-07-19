from django.shortcuts import render, redirect

from django.urls import reverse

import random

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Fighter 

from .forms import StageForm

from .seed_data import characters

# Create your views here.
def home(request):
    return render(request, 'home.html')

def home(request):
    fighters = Fighter.objects.all()
    random_fighter = random.choice(fighters)
    return render(request, 'home.html', {'random_fighter': random_fighter})

def about(request):
  return render(request, 'about.html')

def fighters_index(request):
    fighters = Fighter.objects.all()
    return render(request, 'fighters/index.html', {
       'fighters': fighters
    })

def fighters_detail(request, fighter_id):
  fighter = Fighter.objects.get(id=fighter_id)
  return render(request, 'fighters/detail.html', {
    'fighter': fighter,
    'stage_form': StageForm()
  })

def add_stage(request, fighter_id):
   form = StageForm(request.POST)
   if form.is_valid():
      new_stage = form.save(commit=False)
      new_stage.fighter_id = fighter_id
      new_stage.save()
   return redirect('detail', fighter_id=fighter_id)
# def stage

class FighterCreate(CreateView):
   model = Fighter
   fields = '__all__'

   def get_success_url(self):
      return reverse('detail', kwargs={'fighter_id': self.object.pk})

class FighterUpdate(UpdateView):
   model = Fighter
   fields = ['name', 'image', 'fighter_style', 'move_set', 'description', 'series_name']

class FighterDelete(DeleteView):
   model = Fighter
   success_url = '/fighters'