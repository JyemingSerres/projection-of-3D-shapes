"""
Created on 12/16/2024
by Jye-Ming Serres
"""
import pygame
from pygame.time import Clock

from camera_controller import CameraController, CamEvent
from world import World
from display import Display


class Engine:
    """
    Acts as the main controller of the program
    """

    def __init__(self, world: World, display: Display, clock: Clock) -> None:
        self.running = True
        self.clock = clock
        self.world = world
        self.display = display
        self.cam_control = CameraController(self.world.camera)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    match event.key:
                        # stop running when ESC key is pressed down
                        case pygame.K_ESCAPE: self.running = False
                        # camera translation
                        case pygame.K_a: self.cam_control.translate_event(CamEvent.LEFT_SHIFT)
                        case pygame.K_d: self.cam_control.translate_event(CamEvent.RIGHT_SHIFT)
                        case pygame.K_s: self.cam_control.translate_event(CamEvent.BACKWARD_SHIFT)
                        case pygame.K_w: self.cam_control.translate_event(CamEvent.FORWARD_SHIFT)
                        case pygame.K_SPACE: self.cam_control.translate_event(CamEvent.UP_SHIFT)
                        case pygame.K_LSHIFT: self.cam_control.translate_event(CamEvent.DOWN_SHIFT)
                case pygame.KEYUP:
                    match event.key:
                        # camera translation
                        case pygame.K_a: self.cam_control.translate_event(CamEvent.RIGHT_SHIFT)
                        case pygame.K_d: self.cam_control.translate_event(CamEvent.LEFT_SHIFT)
                        case pygame.K_s: self.cam_control.translate_event(CamEvent.FORWARD_SHIFT)
                        case pygame.K_w: self.cam_control.translate_event(CamEvent.BACKWARD_SHIFT)
                        case pygame.K_SPACE: self.cam_control.translate_event(CamEvent.DOWN_SHIFT)
                        case pygame.K_LSHIFT: self.cam_control.translate_event(CamEvent.UP_SHIFT)
        # camera rotation
        self.cam_control.rotate_event(pygame.mouse.get_rel())

    def update_world(self, milliseconds: int) -> None:
        # execute code from camera controller
        self.cam_control.update()

        # update the model
        dt = milliseconds / 1000
        self.world.update(dt)

    def render(self) -> None:
        self.display.draw(self.world, self.clock.get_fps())
        pygame.display.flip()
