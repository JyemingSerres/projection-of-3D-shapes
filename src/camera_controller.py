"""
Created on 12/20/2024
by Jye-Ming Serres
"""
from enum import Enum, unique
from pygame import Vector3

from state_machine import State, StateMachine
from camera import Camera


@unique
class CamEvent(Enum):
    LEFT_SHIFT = 1,
    RIGHT_SHIFT = 2,
    FORWARD_SHIFT = 3,
    BACKWARD_SHIFT = 4,
    UP_SHIFT = 5,
    DOWN_SHIFT = 6


class CameraController:
    """
    CameraController doc
    """

    def __init__(self, camera: Camera) -> None:
        self.camera = camera
        self.look_sens = 0.1
        self.speed = 400
        self.rel_direction = Vector3(0, 0, 0) # relative to camera's point of view

        # lateral translation state machine
        lateral_neutral = SCamLateralNeutral(self)
        lateral_left = SCamLateralLeft(self)
        lateral_right = SCamLateralRight(self)
        self.sm_lateral = StateMachine([lateral_neutral, lateral_left, lateral_right])
        self.sm_lateral.add_transition(lateral_neutral, lateral_left, CamEvent.LEFT_SHIFT)
        self.sm_lateral.add_transition(lateral_left, lateral_neutral, CamEvent.RIGHT_SHIFT)
        self.sm_lateral.add_transition(lateral_neutral, lateral_right, CamEvent.RIGHT_SHIFT)
        self.sm_lateral.add_transition(lateral_right, lateral_neutral, CamEvent.LEFT_SHIFT)

        # medial translation state machine
        medial_neutral = SCamMedialNeutral(self)
        medial_front = SCamMedialFront(self)
        medial_back = SCamMedialBack(self)
        self.sm_medial = StateMachine([medial_neutral, medial_front, medial_back])
        self.sm_medial.add_transition(medial_neutral, medial_front, CamEvent.FORWARD_SHIFT)
        self.sm_medial.add_transition(medial_front, medial_neutral, CamEvent.BACKWARD_SHIFT)
        self.sm_medial.add_transition(medial_neutral, medial_back, CamEvent.BACKWARD_SHIFT)
        self.sm_medial.add_transition(medial_back, medial_neutral, CamEvent.FORWARD_SHIFT)

        # vertical translation state machine
        vertical_neutral = SCamVerticalNeutral(self)
        vertical_up = SCamVerticalUp(self)
        vertical_down = SCamVerticalDown(self)
        self.sm_vertical = StateMachine([vertical_neutral, vertical_up, vertical_down])
        self.sm_vertical.add_transition(vertical_neutral, vertical_up, CamEvent.UP_SHIFT)
        self.sm_vertical.add_transition(vertical_up, vertical_neutral, CamEvent.DOWN_SHIFT)
        self.sm_vertical.add_transition(vertical_neutral, vertical_down, CamEvent.DOWN_SHIFT)
        self.sm_vertical.add_transition(vertical_down, vertical_neutral, CamEvent.UP_SHIFT)

    def translate_event(self, event: CamEvent) -> None:
        self.sm_lateral.trigger(event)
        self.sm_medial.trigger(event)
        self.sm_vertical.trigger(event)

    def rotate_event(self, mouse_motion: tuple[int, int]) -> None:
        self.camera.angular_velocity = -self.look_sens*Vector3(mouse_motion[0], mouse_motion[1], 0)

    def update(self) -> None:
        self.sm_lateral.update()
        self.sm_medial.update()
        self.sm_vertical.update()
        if self.rel_direction.length() == 0:
            self.camera.velocity = Vector3(0, 0, 0)
        else:
            rel_vel = self.speed * self.rel_direction.normalize()
            self.camera.velocity =  (rel_vel.x*self.camera.orientation
                                     - rel_vel.y*self.camera.image_x
                                     + rel_vel.z*self.camera.image_y)


class SCam(State):
    """
    SCam doc
    """

    def __init__(self, camera_controller: CameraController) -> None:
        super().__init__()
        self.camera_controller = camera_controller

    def enter(self) -> None: pass

    def update(self) -> None: pass

    def exit(self) -> None: pass


# lateral translation
class SCamLateralLeft(SCam):
    def enter(self) -> None:
        self.camera_controller.rel_direction.y = 1


class SCamLateralRight(SCam):
    def enter(self) -> None:
        self.camera_controller.rel_direction.y = -1


class SCamLateralNeutral(SCam):
    def enter(self) -> None:
        self.camera_controller.rel_direction.y = 0


# medial translation
class SCamMedialFront(SCam):
    def enter(self) -> None:
        self.camera_controller.rel_direction.x = 1


class SCamMedialBack(SCam):
    def enter(self) -> None:
        self.camera_controller.rel_direction.x = -1


class SCamMedialNeutral(SCam):
    def enter(self) -> None:
        self.camera_controller.rel_direction.x = 0


# vertical translation
class SCamVerticalUp(SCam):
    def enter(self) -> None:
        self.camera_controller.rel_direction.z = 1


class SCamVerticalDown(SCam):
    def enter(self) -> None:
        self.camera_controller.rel_direction.z = -1


class SCamVerticalNeutral(SCam):
    def enter(self) -> None:
        self.camera_controller.rel_direction.z = 0

