#Game Setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT_SIZE = 18
UI_FONT = '../Assets/font/Winkle-Regular.ttf'

#general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

#weapons 
weapon_data = {
    'excalibur' : {'cooldown' : 100, 'damage' : 15 ,'graphic' : '../Assets/weapon/excalibur/full-up.png'}
    }

#skill
magic_data = {
    'crescent' : {'strength' : 5, 'cost' : 20, 'graphic': '../Assets/particles//crescent/crescent.png'},
    'fireball' : {'strength' : 15, 'cost' : 30, 'graphic' : '../Assets/particles/fireball/fireball.png'}
}

#enemy
monster_data = {
    'beetle' : {'health' : 100 ,'exp' : 50, 'damage' : 8, 'attack_type' : 'slash', 'attack_sound' : '../audio/attack/slash.wav','speed' : 3, 'resistance' : 3, 'attack_radius' : 80, 'notice_radius' : 360 },
    'maggot' : {'health' : 70 ,'exp' : 45, 'damage' : 11, 'attack_type' : 'venom', 'attack_sound' : '../audio/attack/venom.wav', 'speed' : 3, 'resistance' : 3, 'attack_radius' : 100, 'notice_radius' : 360  },
    'wyrm' : {'health' : 250 ,'exp' : 250, 'damage' : 30, 'attack_type' : 'thunder', 'attack_sound' : '../audio/attack/fire.wav','speed' : 2, 'resistance' : 120, 'attack_radius' : 80, 'notice_radius' : 360  }
}