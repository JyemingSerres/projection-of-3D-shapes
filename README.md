# Projection of 3D shapes
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
## Introduction
The goal of this exercise is to display 3D shapes onto a 2D screen using 3-point perspective. Using mouse and keyboard inputs, the user is able to travel across space to inspect objects at various angles and distances.

![An execution displaying the platonic solids in different colors](/assets/screenshot_execution.png)
## Theoretical background
This project uses the [pinhole camera model](https://en.m.wikipedia.org/wiki/Pinhole_camera_model). An image's size is inversely proportional to the object's perpendicular distance from the image plane but is otherwise a simple orthogonal projection. In this program, a shape is defined by a set of vectors representing the position of its vertices and edges are tracked amidst manipulations by an association table of vertices.
## Limitations
Shapes are only displayed if all of their vertices are in front of the virtual camera's aperture, meaning the nearest shapes within the rendering frame can suddently stop rendering and effectively disappear when moving the camera.

The processing power required to display a shape is mostly independent of distance. This implies that the size of the simulation is directly limited by the number of shapes.
## Dependencies
pygame 2.6.1 (SDL 2.28.4, Python 3.10.6)
