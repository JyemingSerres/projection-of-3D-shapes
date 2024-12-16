"""
Created on 12/15/2024
by Jye-Ming Serres
"""
from pygame import Vector3

class Camera:
    """
    Camera doc
    """
    DEFAULT_ORIENTATION = Vector3(1, 0, 0)

    def __init__(self, center: Vector3=Vector3(0, 0, 0), pupil_distance: float=100) -> None:
        # center is the principal point / image center
        self.center = center
        # TODO: this vector should be normalized
        self.orientation = Camera.DEFAULT_ORIENTATION
        self.pupil_distance = pupil_distance
        self.pupil = center - self.pupil_distance*self.orientation
    
