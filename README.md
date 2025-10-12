# Projection of 3D shapes
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
## Introduction
The goal of this exercise is to display 3D shapes onto a 2D screen using 3-point perspective. Using mouse and keyboard inputs, the user is able to travel across space to inspect objects at various angles.

![An execution displaying the platonic solids in different colors](/assets/execution.gif)
## Theoretical background
This project uses the [pinhole camera model](https://en.m.wikipedia.org/wiki/Pinhole_camera_model). An image's size is inversely proportional to the object's perpendicular distance from the image plane but is otherwise a simple orthogonal projection. In this program, a shape is defined by a list of vectors, each of which represents the position of a vertex

## Limitations
Shapes are only displayed if all of their vertices are in front of the virtual camera's aperture, meaning the nearest shapes within the rendering frame can suddently stop rendering and effectively disappear when moving the camera.

The computational power required to display a shape is mostly independent of distance. That is to say, the processing load scales linearly with the amount of shapes.
## Dependencies
pygame 2.6.1 (SDL 2.28.4, Python 3.10.6)
