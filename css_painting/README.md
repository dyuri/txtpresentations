# CSS Painting API

One of the new CSS Houdini APIs:

- CSS Parser API - possibility to implement sass/less/etc support
- CSS Properties and Values API - more advanced CSS properties (variables)
- CSS Typed OM - CSS values as typed  JS objects
- CSS Layout API - create custom layouts (like grid or flexbox)
- CSS Painting API - draw something in CSS

## Concept

Allows developers to create custom functions for `paint()` to draw images for CSS (where they can be used, like backgrounds, border images, ...).

## Usage

- define a paint worklet using `registerPaint()`
- register the worklet
- use it in your CSS

## Demo

See [demo.html](demo.html)