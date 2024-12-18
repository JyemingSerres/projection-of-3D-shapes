"""
Created on 12/16/2024
by Jye-Ming Serres
"""
import pygame
from pygame.event import Event
from pygame.time import Clock
from enum import Enum

from state import State, StateMachine
from world import World
from camera import Camera
from display import Display

class Input(Enum):
    DOWN_a = 1,
    DOWN_d = 2,
    DOWN_s = 3,
    DOWN_w = 4,
    DOWN_SPACE = 5,
    DOWN_LSHIFT = 6,
    UP_a = 5,
    UP_d = 6,
    UP_s = 7,
    UP_w = 8,
    UP_SPACE = 9,
    UP_LSHIFT = 10

class Engine:
    """
    Controller doc
    """

    def __init__(self, world: World, display: Display, clock: Clock) -> None:
        self.world = world
        self.display = display
        self.clock = clock

        lateral_neutral = SCamLateralNeutral(self.world.camera)
        lateral_left = SCamLateralLeft(self.world.camera)
        lateral_right = SCamLateralRight(self.world.camera)
        self.sm_lateral = StateMachine([lateral_neutral, lateral_left, lateral_right])
        self.sm_lateral.add_transitions(lateral_neutral, lateral_left, [Input.DOWN_a, Input.UP_d])
        self.sm_lateral.add_transitions(lateral_left, lateral_neutral, [Input.DOWN_d, Input.UP_a])
        self.sm_lateral.add_transitions(lateral_neutral, lateral_right, [Input.DOWN_d, Input.UP_a])
        self.sm_lateral.add_transitions(lateral_right, lateral_neutral, [Input.DOWN_a, Input.UP_d])

        medial_neutral = SCamMedialNeutral(self.world.camera)
        medial_front = SCamMedialFront(self.world.camera)
        medial_back = SCamMedialBack(self.world.camera)
        self.sm_medial = StateMachine([medial_neutral, medial_front, medial_back])
        self.sm_medial.add_transitions(medial_neutral, medial_front, [Input.DOWN_w, Input.UP_s])
        self.sm_medial.add_transitions(medial_front, medial_neutral, [Input.DOWN_s, Input.UP_w])
        self.sm_medial.add_transitions(medial_neutral, medial_back, [Input.DOWN_s, Input.UP_w])
        self.sm_medial.add_transitions(medial_back, medial_neutral, [Input.DOWN_w, Input.UP_s])

        vertical_neutral = SCamVerticalNeutral(self.world.camera)
        vertical_up = SCamVerticalUp(self.world.camera)
        vertical_down = SCamVerticalDown(self.world.camera)
        self.sm_vertical = StateMachine([vertical_neutral, vertical_up, vertical_down])
        self.sm_vertical.add_transitions(vertical_neutral, vertical_up, [Input.DOWN_SPACE, Input.UP_LSHIFT])
        self.sm_vertical.add_transitions(vertical_up, vertical_neutral, [Input.DOWN_LSHIFT, Input.UP_SPACE])
        self.sm_vertical.add_transitions(vertical_neutral, vertical_down, [Input.DOWN_LSHIFT, Input.UP_SPACE])
        self.sm_vertical.add_transitions(vertical_down, vertical_neutral, [Input.DOWN_SPACE, Input.UP_LSHIFT])

    def handle_event(self, event: Event) -> None:
        match event.type:
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_w:
                        self.sm_medial.trigger(Input.DOWN_w)
                    case pygame.K_a:
                        self.sm_lateral.trigger(Input.DOWN_a)
                    case pygame.K_s:
                        self.sm_medial.trigger(Input.DOWN_s)
                    case pygame.K_d:
                        self.sm_lateral.trigger(Input.DOWN_d)
                    case pygame.K_SPACE:
                        self.sm_vertical.trigger(Input.DOWN_SPACE)
                    case pygame.K_LSHIFT:
                        self.sm_vertical.trigger(Input.DOWN_LSHIFT)
            case pygame.KEYUP:
                match event.key:
                    case pygame.K_w:
                        self.sm_medial.trigger(Input.UP_w)
                    case pygame.K_a:
                        self.sm_lateral.trigger(Input.UP_a)
                    case pygame.K_s:
                        self.sm_medial.trigger(Input.UP_s)
                    case pygame.K_d:
                        self.sm_lateral.trigger(Input.UP_d)
                    case pygame.K_SPACE:
                        self.sm_vertical.trigger(Input.UP_SPACE)
                    case pygame.K_LSHIFT:
                        self.sm_vertical.trigger(Input.UP_LSHIFT)
    
    def update_world(self) -> None:
        self.sm_medial.update()
        self.sm_lateral.update()
        self.sm_vertical.update()
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

class SCamLateralLeft(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.y = 1

class SCamLateralRight(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.y = -1

class SCamLateralNeutral(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.y = 0

class SCamMedialFront(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.x = 1

class SCamMedialBack(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.x = -1

class SCamMedialNeutral(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.x = 0

class SCamVerticalUp(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.z = 1

class SCamVerticalDown(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.z = -1

class SCamVerticalNeutral(SCam):
    def enter(self) -> None:
        self.camera.rel_velocity.z = 0