from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Fighter 

from .forms import StageForm



# fighters = [

#     {
#         'name': 'Mario',
#         'image': 'mario.png',
#         'series_name': 'Super Mario',
#         'fighter_style': 'All-Rounder',
#         'move_set': 'Fireball, Super Jump Punch, Cape',
#         'description': 'The iconic plumber from the Mushroom Kingdom.',
#         'series_id': 1,
#     },
#     {
#         'name': 'Link',
#         'image': 'link.png',
#         'series_name': 'The Legend of Zelda',
#         'fighter_style': 'Swordfighter',
#         'move_set': "Hero's Bow, Spin Attack, Bomb",
#         'description': 'The hero clad in green who wields the Master Sword.',
#         'series_id': 2,
#     },
#     {
#         'name': 'Samus',
#         'image': 'samus.png',
#         'series_name': 'Metroid',
#         'fighter_style': 'Projectile-based',
#         'move_set': 'Charge Shot, Missile, Screw Attack',
#         'description': 'The intergalactic bounty hunter in her armored suit.',
#         'series_id': 3,
#     },
#     {
#         'name': 'Pikachu',
#         'image': 'pikachu.png',
#         'series_name': 'Pokémon',
#         'fighter_style': 'Agile Electric',
#         'move_set': 'Thunder Jolt, Quick Attack, Thunder',
#         'description': 'The lovable electric rodent and mascot of Pokémon.',
#         'series_id': 4,
#     },
#     {
#         'name': 'Donkey Kong',
#         'image': 'donkey_kong.png',
#         'series_name': 'Donkey Kong',
#         'fighter_style': 'Powerful Brawler',
#         'move_set': 'Giant Punch, Spinning Kong, Headbutt',
#         'description': 'The king of the jungle with incredible strength.',
#         'series_id': 5,
#     },
# ]

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