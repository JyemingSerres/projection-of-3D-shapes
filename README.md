# Projection of 3D shapes
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
## Introduction
The goal of this exercise is to display 3D shapes onto a 2D screen. Using mouse and keyboard inputs, the user is able to travel across space to inspect objects at various angles.

![Video of the executable running displaying platonic solids in different colors](/assets/execution.gif)
## Theoretical background
This project uses the [pinhole camera model](https://en.m.wikipedia.org/wiki/Pinhole_camera_model). A point's image can be seen as the orthogonal projection of the point onto an image plane. Though its distance from the plane's origin (image center) is inversely proportional to the point's shortest distance from the plane. In this program, a shape is defined by a list of vectors, each of which represents the position of a vertex. Edges are represented by an association table of vertices.

## Limitations
Shapes are only displayed if all of their vertices are in front of the image plane, meaning the nearest shapes within the rendering frame can effectively disappear.

All shapes before the image plane, even those entirely outside the rendering frame, have their projection computed every frame.

Shapes will require mostly the same amount of computation whether they are far or near. There is no precision loss or reduction in [level of detail](https://en.wikipedia.org/wiki/Level_of_detail_(computer_graphics)) based on how far the shape is to lighten the computational load.

## Dependencies
- pygame 2.6.1 (SDL 2.28.4, Python 3.10.6)
- pylint 3.3.2
- pyinstaller 6.16.0
