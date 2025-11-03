# Projection of 3D shapes
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
## Introduction
The goal of this exercise is to display 3D shapes onto a 2D screen using 3-point perspective. Using mouse and keyboard inputs, the user is able to travel across space to inspect objects at various angles.

![Video of the executable running displaying platonic solids in different colors](/assets/execution.gif)
## Theoretical background
This project uses the [pinhole camera model](https://en.m.wikipedia.org/wiki/Pinhole_camera_model). A point's image is its orthogonal projection onto an image plane except that the image's distance from the plane's origin is inversely proportional to the object's perpendicular distance from said plane. In this program, a shape is defined by a list of vectors, each of which represents the position of a vertex. Edges are represented by an association table of vertices.

## Limitations
Shapes are only displayed if all of their vertices are in front of the image plane, meaning the nearest shapes within the rendering frame can effectively disappear at certain angles.

Shapes will require mostly the same amount of computation whether they are far or near. The computational load scales linearly with the quantity of shapes within the rendering frame.

## Dependencies
- pygame 2.6.1 (SDL 2.28.4, Python 3.10.6)
- pylint 3.3.2
- pyinstaller 6.16.0