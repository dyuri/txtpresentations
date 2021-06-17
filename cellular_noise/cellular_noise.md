# Cellular noise

## Random points

- true randomness is hard
- pseudo random number generators usually don't have even distribution
  - or "slow"
  - or cannot be used in a parallel way
- OpenGL does not have random API (reasons above)

And in most cases higher "entropy" is more pleasant to the eyes.

"Solution": **cellular noise**

- divide the space into cells
- pick one random point in each cell
- profit - can be processed in a parallel way very efficiently

[Classic, canvas based example](./css_paint.html) using the CSS Paint API.

## Classic (canvas) vs. shader approach

**Classic**:

- set pixel colors, draw lines / arcs, fill them
- more pixels/shapes to draw => more time required
- hard to do in a parallel way

**Shader:**

- you get all the pixels (on a vertex), you have to determine the color of each
- more complex graphics => more time, BUT you *need* to set the color of all the pixels anyway
- **very** easy to do in a parallel way

[Live demo](https://www.shadertoy.com/view/Nt2GDW)
