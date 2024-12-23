# Projection of 3D shapes
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
## Introduction
The goal of this exercise is to display 3D shapes onto a 2D screen following human eyesight perspective. Using mouse and keyboard inputs, the user is able to travel accross space to inspect objects at various angles and distance.
## Theoretical background
This project uses the [pinhole camera model](https://en.m.wikipedia.org/wiki/Pinhole_camera_model), a simple yet effective model to simulate eyesight. Object image is inversely proportional to their distance to the camera aperture but is otherwise a simple orthogonal projection onto an image plane. Shapes are defined by a set of vectors representing the position of their vertices and an association table between those vertices to keep track of the edges.
## Dependencies
pygame 2.6.1 (SDL 2.28.4, Python 3.10.6)
