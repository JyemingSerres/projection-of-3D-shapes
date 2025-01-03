# Projection of 3D shapes
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
## Introduction
The goal of this exercise is to display 3D shapes onto a 2D screen with human eyesight perspective. Using mouse and keyboard inputs, the user is able to travel across space to inspect objects at various angles and distances.
## Theoretical background
This project uses the [pinhole camera model](https://en.m.wikipedia.org/wiki/Pinhole_camera_model). An object's image is inversely proportional to its distance to the camera aperture but is otherwise a simple orthogonal projection onto an image plane. In this program, a shape is defined by a set of vectors representing the position of its vertices and edges are being tracked amidst calculations by an association table between the vertices.
## Limitations
Shapes are only displayed if all of their vertices are in front of the virtual camera's aperture, meaning shapes within the rendering frame can effectively disappear at runtime.
Every shape displayed within the rendering frame require the same amount of processing power regardless of their distance.
## Dependencies
pygame 2.6.1 (SDL 2.28.4, Python 3.10.6)
