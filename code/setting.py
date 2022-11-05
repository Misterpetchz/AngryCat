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

#weapons 
weapon_data = {
    'excalibur' : {'cooldown' : 100, 'damage' : 15 ,'graphic' : '../Assets/weapon/excalibur/full-up.png'}
    }

#skill
magic_data = {
    'crescent' : {'strength' : 5, 'cost' : 20, 'graphic': '../Assets/particles//crescent/crescent.png'},
    'fireball' : {'strength' : 15, 'cost' : 30, 'graphic' : '../Assets/particles/fireball/fireball.png'}
}