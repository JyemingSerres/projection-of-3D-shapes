"""
Created on 12/16/2024
by Jye-Ming Serres
"""
import pygame
from pygame.event import Event
from pygame.time import Clock
from enum import Enum

# Project modules
from config import *
from state import State, StateMachine
from world import World
from camera import Camera
from display import Display

class SEvent(Enum):
    LEFT_SHIFT = 1,
    RIGHT_SHIFT = 2,
    FORWARD_SHIFT = 3,
    BACKWARD_SHIFT = 4,
    UP_SHIFT = 5,
    DOWN_SHIFT = 6

class Engine:
    """
    Acts as the controller of the program
    """

    def __init__(self, world: World, display: Display, clock: Clock) -> None:
        self.running = True

        self.world = world
        self.display = display
        self.clock = clock

        self.CAMERA_SENSITIVITY = 0.1

        # camera lateral movement
        lateral_neutral = SCamLateralNeutral(self.world.camera)
        lateral_left = SCamLateralLeft(self.world.camera)
        lateral_right = SCamLateralRight(self.world.camera)
        self.sm_lateral = StateMachine([lateral_neutral, lateral_left, lateral_right])
        self.sm_lateral.add_transition(lateral_neutral, lateral_left, SEvent.LEFT_SHIFT)
        self.sm_lateral.add_transition(lateral_left, lateral_neutral, SEvent.RIGHT_SHIFT)
        self.sm_lateral.add_transition(lateral_neutral, lateral_right, SEvent.RIGHT_SHIFT)
        self.sm_lateral.add_transition(lateral_right, lateral_neutral, SEvent.LEFT_SHIFT)

        # camera medial movement
        medial_neutral = SCamMedialNeutral(self.world.camera)
        medial_front = SCamMedialFront(self.world.camera)
        medial_back = SCamMedialBack(self.world.camera)
        self.sm_medial = StateMachine([medial_neutral, medial_front, medial_back])
        self.sm_medial.add_transition(medial_neutral, medial_front, SEvent.FORWARD_SHIFT)
        self.sm_medial.add_transition(medial_front, medial_neutral, SEvent.BACKWARD_SHIFT)
        self.sm_medial.add_transition(medial_neutral, medial_back, SEvent.BACKWARD_SHIFT)
        self.sm_medial.add_transition(medial_back, medial_neutral, SEvent.FORWARD_SHIFT)

        # camera vertical movement
        vertical_neutral = SCamVerticalNeutral(self.world.camera)
        vertical_up = SCamVerticalUp(self.world.camera)
        vertical_down = SCamVerticalDown(self.world.camera)
        self.sm_vertical = StateMachine([vertical_neutral, vertical_up, vertical_down])
        self.sm_vertical.add_transition(vertical_neutral, vertical_up, SEvent.UP_SHIFT)
        self.sm_vertical.add_transition(vertical_up, vertical_neutral, SEvent.DOWN_SHIFT)
        self.sm_vertical.add_transition(vertical_neutral, vertical_down, SEvent.DOWN_SHIFT)
        self.sm_vertical.add_transition(vertical_down, vertical_neutral, SEvent.UP_SHIFT)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                # stop running when encountering a pygame.QUIT event
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    match event.key:
                        # camera movement
                        case pygame.K_w:
                            self.sm_medial.trigger(SEvent.FORWARD_SHIFT)
                        case pygame.K_a:
                            self.sm_lateral.trigger(SEvent.LEFT_SHIFT)
                        case pygame.K_s:
                            self.sm_medial.trigger(SEvent.BACKWARD_SHIFT)
                        case pygame.K_d:
                            self.sm_lateral.trigger(SEvent.RIGHT_SHIFT)
                        case pygame.K_SPACE:
                            self.sm_vertical.trigger(SEvent.UP_SHIFT)
                        case pygame.K_LSHIFT:
                            self.sm_vertical.trigger(SEvent.DOWN_SHIFT)
                        # stop running when ESC key is pressed down
                        case pygame.K_ESCAPE:
                            self.running = False
                case pygame.KEYUP:
                    match event.key:
                        # camera movement
                        case pygame.K_w:
                            self.sm_medial.trigger(SEvent.BACKWARD_SHIFT)
                        case pygame.K_a:
                            self.sm_lateral.trigger(SEvent.RIGHT_SHIFT)
                        case pygame.K_s:
                            self.sm_medial.trigger(SEvent.FORWARD_SHIFT)
                        case pygame.K_d:
                            self.sm_lateral.trigger(SEvent.LEFT_SHIFT)
                        case pygame.K_SPACE:
                            self.sm_vertical.trigger(SEvent.DOWN_SHIFT)
                        case pygame.K_LSHIFT:
                            self.sm_vertical.trigger(SEvent.UP_SHIFT)
                case pygame.MOUSEMOTION:
                    offset = event.rel
                    if offset != (0, 0):
                        self.world.camera.angular_velocity = (-self.CAMERA_SENSITIVITY*offset[0], -self.CAMERA_SENSITIVITY*offset[1])
                
    def update_world(self) -> None:
        # execute code from state machines
        self.sm_medial.update()
        self.sm_lateral.update()
        self.sm_vertical.update()
        # update the model
        self.world.update()

    def render(self) -> None:
        self.display.draw(self.world, self.clock)

class SCam(State):
    def __init__(self, camera: Camera) -> None:
        super().__init__()
        self.camera = camera
    
    def enter(self) -> None: pass

    def update(self) -> None: pass

    def exit(self) -> None: pass

# lateral movement
class SCamLateralLeft(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.y = 1

class SCamLateralRight(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.y = -1

class SCamLateralNeutral(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.y = 0

# medial movement
class SCamMedialFront(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.x = 1

class SCamMedialBack(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.x = -1

class SCamMedialNeutral(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.x = 0

# vertical movement
class SCamVerticalUp(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.z = 1

class SCamVerticalDown(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.z = -1

class SCamVerticalNeutral(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.z = 0