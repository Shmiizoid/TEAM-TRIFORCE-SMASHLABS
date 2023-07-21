from django.shortcuts import render, redirect

from django.urls import reverse

import random

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Fighter, Stage 

import requests



# Create your views here.
def home(request):
    fighters = Fighter.objects.all()
    random_fighters = random.sample(list(fighters), 3)
    return render(request, 'home.html', {'random_fighters': random_fighters})

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
  })

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

#Stage 

def stages_index(request):
    stages = Stage.objects.all()
    return render(request, 'stages/index.html', {
        'stages': stages
    })

def stages_detail(request, stage_id):
    stage = Stage.objects.get(id=stage_id)
    return render(request, 'stages/detail.html', {
        'stage': stage,
    })

class StageCreate(CreateView):
    model = Stage
    fields = '__all__'
     
    def get_success_url(self):
        return reverse('stages_detail', kwargs={'stage_id': self.object.pk})

class StageUpdate(UpdateView):
    model = Stage
    fields = '__all__'

    def get_success_url(self):
        return reverse('stages_detail', kwargs={'stage_id': self.object.pk})

class StageDelete(DeleteView):
    model = Stage
    success_url = '/stages'

# API FUNCTIONS

def fetch_characters_data():
    api_url = 'https://raw.githubusercontent.com/leocabeza/smashbros-unofficial-api/master/pages/api/v1/ultimate/characters/characters.json'
    response = requests.get(api_url)
    characters_data = response.json()
    return characters_data

def characters_index(request):
    characters = fetch_characters_data()
    return render(request, 'characters/index.html', {'characters': characters})

def characters_detail(request, character_index):
    characters = fetch_characters_data()
    character = characters[character_index]
    return render(request, 'characters/detail.html', {'character': character})