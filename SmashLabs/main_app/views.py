from django.shortcuts import render, redirect

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

class FighterUpdate(UpdateView):
   model = Fighter
   fields = ['image', 'fighter_style', 'move_set']

class FighterDelete(DeleteView):
   model = Fighter
   success_url = '/fighters'