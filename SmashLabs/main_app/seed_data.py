#Add this code below into views.py to import the fighters list
# from .seed_data import fighters  

characters = [
    {
        'character_id': '001',
        'name': 'Mario',
        'image': 'mario.jpg',
        'fighter_style': 'All-Rounder',
        'move_set': 'Fireball, Super Jump Punch, Cape',
        'description': 'The iconic plumber from the Mushroom Kingdom.',
        'series_name': 'Super Mario Bros.'
    },
    {
        'character_id': '002',
        'name': 'Donkey Kong',
        'image': 'donkey_kong.jpg',
        'fighter_style': 'Powerhouse',
        'move_set': 'Giant Punch, Spinning Kong, Headbutt',
        'description': 'The powerful and barrel-throwing ape.',
        'series_name': 'Donkey Kong'
    },
    {
        'character_id': '003',
        'name': 'Link',
        'image': 'link.jpg',
        'fighter_style': 'Zone-Breaker',
        'move_set': 'Hero\'s Bow, Spin Attack, Boomerang',
        'description': 'The legendary hero of Hyrule.',
        'series_name': 'The Legend of Zelda'
    },
    {
        'character_id': '004',
        'name': 'Samus',
        'image': 'samus.jpg',
        'fighter_style': 'Zoner',
        'move_set': 'Charge Shot, Screw Attack, Missile',
        'description': 'The intergalactic bounty hunter.',
        'series_name': 'Metroid'
    },
    {
        'character_id': '005',
        'name': 'Yoshi',
        'image': 'yoshi.jpg',
        'fighter_style': 'Rushdown',
        'move_set': 'Egg Lay, Yoshi Bomb, Flutter Jump',
        'description': 'The friendly dinosaur from Yoshi\'s Island.',
        'series_name': 'Yoshi'
    },
    {
        'character_id': '006',
        'name': 'Kirby',
        'image': 'kirby.jpg',
        'fighter_style': 'Mix-Up',
        'move_set': 'Inhale, Hammer Flip, Final Cutter',
        'description': 'The pink puffball with the power to absorb abilities.',
        'series_name': 'Kirby'
    },
    {
        'character_id': '007',
        'name': 'Fox',
        'image': 'fox.jpg',
        'fighter_style': 'Rushdown',
        'move_set': 'Blaster, Fox Illusion, Fire Fox',
        'description': 'The agile space-faring fox pilot.',
        'series_name': 'Star Fox'
    },
    {
        'character_id': '008',
        'name': 'Pikachu',
        'image': 'pikachu.jpg',
        'fighter_style': 'Rushdown',
        'move_set': 'Thunder Jolt, Skull Bash, Thunder',
        'description': 'The electric rodent Pokémon.',
        'series_name': 'Pokémon'
    },
    {
        'character_id': '009',
        'name': 'Luigi',
        'image': 'luigi.jpg',
        'fighter_style': 'All-Rounder',
        'move_set': 'Green Fireball, Luigi Cyclone, Super Jump Punch',
        'description': 'Mario\'s taller brother with his own set of moves.',
        'series_name': 'Super Mario Bros.'
    },
    {
        'character_id': '010',
        'name': 'Ness',
        'image': 'ness.jpg',
        'fighter_style': 'Glass Cannon',
        'move_set': 'PK Flash, PK Thunder, PSI Magnet',
        'description': 'The psychic boy from Onett.',
        'series_name': 'Earthbound'
    },
    {
        'character_id': '011',
        'name': 'Captain Falcon',
        'image': 'captain_falcon.jpg',
        'fighter_style': 'Rushdown',
        'move_set': 'Falcon Punch, Raptor Boost, Falcon Dive',
        'description': 'The high-speed bounty hunter and racer.',
        'series_name': 'F-Zero'
    },
    {
        'character_id': '012',
        'name': 'Jigglypuff',
        'image': 'jigglypuff.jpg',
        'fighter_style': 'Hit & Run',
        'move_set': 'Rollout, Rest, Sing',
        'description': 'The melodic and sleepy Pokémon.',
        'series_name': 'Pokémon'
    },
    {
        'character_id': '013',
        'name': 'Peach',
        'image': 'peach.jpg',
        'fighter_style': 'Mix-Up',
        'move_set': 'Toad, Peach Bomber, Peach Parasol',
        'description': 'The elegant princess of the Mushroom Kingdom.',
        'series_name': 'Super Mario Bros.'
    },
    {
        'character_id': '014',
        'name': 'Bowser',
        'image': 'bowser.jpg',
        'fighter_style': 'Powerhouse',
        'move_set': 'Bowser Bomb, Whirling Fortress, Flying Slam',
        'description': 'The monstrous king of the Koopas.',
        'series_name': 'Super Mario Bros.'
    },
    {
        'character_id': '015',
        'name': 'Ice Climbers',
        'image': 'ice_climbers.jpg',
        'fighter_style': 'Tag Team',
        'move_set': 'Ice Shot, Squall Hammer, Blizzard',
        'description': 'The duo of climbers on a chilly adventure.',
        'series_name': 'Ice Climber'
    },
    {
        'character_id': '016',
        'name': 'Sheik',
        'image': 'sheik.jpg',
        'fighter_style': 'Dynamic',
        'move_set': 'Needle Storm, Vanish, Bouncing Fish',
        'description': 'The swift and elusive warrior.',
        'series_name': 'The Legend of Zelda'
    },
    {
        'character_id': '017',
        'name': 'Zelda',
        'image': 'zelda.jpg',
        'fighter_style': 'Dynamic',
        'move_set': 'Nayru\'s Love, Din\'s Fire, Farore\'s Wind',
        'description': 'The wise and magical princess of Hyrule.',
        'series_name': 'The Legend of Zelda'
    },
    {
        'character_id': '018',
        'name': 'Dr. Mario',
        'image': 'dr_mario.jpg',
        'fighter_style': 'All-Rounder',
        'move_set': 'Megavitamin, Super Sheet, Super Jump Punch',
        'description': 'Mario\'s alter ego with medical skills.',
        'series_name': 'Super Mario Bros.'
    },
    {
        'character_id': '019',
        'name': 'Pichu',
        'image': 'pichu.jpg',
        'fighter_style': 'Glass Cannon',
        'move_set': 'Thunder Jolt, Skull Bash, Thunder',
        'description': 'A smaller and cuter version of Pikachu.',
        'series_name': 'Pokémon'
    },
    {
        'character_id': '020',
        'name': 'Falco',
        'image': 'falco.jpg',
        'fighter_style': 'Rushdown',
        'move_set': 'Blaster, Falco Phantasm, Fire Bird',
        'description': 'Fox\'s avian wingman with his own style.',
        'series_name': 'Star Fox'
    },
    {
        'character_id': '021',
        'name': 'Marth',
        'image': 'marth.jpg',
        'fighter_style': 'Footsies',
        'move_set': 'Shield Breaker, Dancing Blade, Counter',
        'description': 'The prince of Altea and a master of the sword.',
        'series_name': 'Fire Emblem'
    },
    {
        'character_id': '022',
        'name': 'Young Link',
        'image': 'young_link.jpg',
        'fighter_style': 'Rushdown',
        'move_set': 'Fire Bow, Spin Attack, Boomerang',
        'description': 'A younger version of Link with quick moves.',
        'series_name': 'The Legend of Zelda'
    },
    {
        'character_id': '023',
        'name': 'Ganondorf',
        'image': 'ganondorf.jpg',
        'fighter_style': 'Powerhouse',
        'move_set': 'Warlock Punch, Gerudo Dragon, Wizard\'s Foot',
        'description': 'The embodiment of evil and Link\'s nemesis.',
        'series_name': 'The Legend of Zelda'
    },
    {
        'character_id': '024',
        'name': 'Mewtwo',
        'image': 'mewtwo.jpg',
        'fighter_style': 'Zone-Breaker',
        'move_set': 'Shadow Ball, Confusion, Disable',
        'description': 'The powerful and mysterious psychic Pokémon.',
        'series_name': 'Pokémon'
    },
    {
        'character_id': '025',
        'name': 'Roy',
        'image': 'roy.jpg',
        'fighter_style': 'Rushdown',
        'move_set': 'Flare Blade, Double-Edge Dance, Counter',
        'description': 'A noble swordsman from Fire Emblem: The Binding Blade.',
        'series_name': 'Fire Emblem'
    }
]
