import pygame
from support import import_folder

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            #magic
            'crescent' : import_folder('../Assets/particles/crescent/frames'),
            'fireball' : import_folder('../Assets/particles/fireball/frames'),

            #attacks
            'slash' : import_folder('../Assets/particles/slash'),
            'thunder' : import_folder('../Assets/particles/thunder'),
            'venom' : import_folder('../Assets/particles/venom'),

            #monster deaths
            'wyrm' : import_folder('../Assets/particles/shatter'),
            'beetle' : import_folder('../Assets/particles/nova'),
            'maggot' : import_folder('../Assets/particles/dissolve')
        }

    def reflect_images(self, frames):
        new_frames = []

        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.image.get_rect[self.frame_index]

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()