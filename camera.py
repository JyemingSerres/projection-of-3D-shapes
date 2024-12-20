"""
Created on 12/15/2024
by Jye-Ming Serres
"""
from pygame import Vector3

class Camera:
    """
    Camera doc
    """

    def __init__(self, aperture: Vector3=Vector3(0, 0, 0), image_plane_dist: float=360) -> None:
        self._aperture = aperture
        self._image_x_vect = Vector3(0, -1, 0) # normalized vector
        self._image_y_vect = Vector3(0, 0, 1) # normalized vector
        self._orientation = self._calculate_orientation() # normalized vector
        self._image_plane_dist = image_plane_dist # will influence FOV since the size of the plane is finite and constant

        self.SPEED = 4
        self.rel_velocity = Vector3(0, 0, 0) # relative to our own point of view (looking towards orientation)
        self.angular_velocity = (0, 0) # TODO: not really the angular velocity but contains the same information
    
    @property
    def aperture(self) -> Vector3:
        return self._aperture

    @property
    def image_x_vect(self) -> Vector3:
        return self._image_x_vect

    @property
    def image_y_vect(self) -> Vector3:
        return self._image_y_vect

    @property
    def orientation(self) -> Vector3:
        return self._orientation

    @property
    def image_plane_dist(self) -> float:
        return self._image_plane_dist

    def update(self) -> None:
        if self.rel_velocity.length() != 0:
            direction = self.rel_velocity.normalize()
            velocity = self.SPEED * (direction.x*self._orientation - direction.y*self.image_x_vect + direction.z*self.image_y_vect)
            self.move(velocity)

        self.image_x_vect.rotate_ip(self.angular_velocity[0], self.image_y_vect)
        self.image_y_vect.rotate_ip(self.angular_velocity[1], self.image_x_vect)
        self._orientation = self._calculate_orientation()
        self.angular_velocity = (0, 0) # TODO: dirty code

    def move(self, velocity: Vector3) -> None:
        self._aperture += velocity

    def _calculate_orientation(self) -> Vector3:
        # orientation vector is the vector normal to the projection plane
        return self._image_y_vect.cross(self._image_x_vect).normalize()
