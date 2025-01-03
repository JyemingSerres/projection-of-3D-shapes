"""
"""

from pygame import Vector3

__author__ = "Jye-Ming Serres"


class Camera:
    """
    Camera doc
    """

    def __init__(self, aperture: Vector3 = Vector3(0, 0, 0), focal_length: float = 360) -> None:
        self._aperture = aperture # also acts as the position of the camera
        self._image_x = Vector3(0, -1, 0) # normalized
        self._image_y = Vector3(0, 0, 1) # normalized
        self._orientation = self._calculate_orientation() # normalized
        self._focal_length = focal_length # will influence FOV

        self.velocity = Vector3(0, 0, 0)
        # angular velocity with respect to image_y, image_x then orientation, in that order
        self.angular_velocity = Vector3(0, 0, 0) # in degrees

    @property
    def aperture(self) -> Vector3:
        return self._aperture

    @property
    def image_x(self) -> Vector3:
        return self._image_x

    @property
    def image_y(self) -> Vector3:
        return self._image_y

    @property
    def orientation(self) -> Vector3:
        return self._orientation

    @property
    def focal_length(self) -> float:
        return self._focal_length

    def update(self, dt: float) -> None:
        self.move(self.velocity * dt)
        self.rotate(self.angular_velocity)

    def move(self, displacement: Vector3) -> None:
        self._aperture += displacement

    def rotate(self, angular_displacement: Vector3) -> None:
        self._image_x.rotate_ip(angular_displacement[0], self._image_y)
        self._image_y.rotate_ip(angular_displacement[1], self._image_x)
        self._orientation = self._calculate_orientation()
        self._image_x.rotate_ip(angular_displacement[2], self._orientation)
        self._image_y.rotate_ip(angular_displacement[2], self._orientation)

    def _calculate_orientation(self) -> Vector3:
        # orientation vector is a vector normal to the projection plane (principal plane)
        return self._image_y.cross(self._image_x).normalize()
