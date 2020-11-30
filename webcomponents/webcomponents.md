# Web Components

- reusable custom elements
- framework independent
- standardized

## Related standards

### Custom Elements

JS API to define custom HTML elements.

### Shadow DOM

JS API to attach encapsulated "shadow" DOM to an element, which will be "separated" from the main document.
This way the elements styles, events, "shadow" children could be kept "private", and won't collide with the main document's styles, etc.

### HTML templates

`<template>` and `<slot>` elements

## Basic approach

- create a class for the web component, inherit from `HTMLElement` (or descendants) for best result
- register your element using `CustomElementRegistry.define()`
- attach a shadow DOM if required using `Element.attachShadow()`
- you can use `<template>` and `<slot>` for the content
- use your new element wherever you like as any regular HTML element

## Support

*Almost* all the browsers support them. (Even IE11 w/ polyfill.)

*Almost* all modern framework could handle web components as they were standard HTML elements, and lot of them are capable of _exporting_ their own components as standard web compononents.

https://custom-elements-everywhere.com/

## What's next?

- scoped custom element registry - to avoid name collisions
- constructable stylesheets - attach/manipulate styles to a (shadow) DOM tree more easily
- CSS modules - `import` CSS into JS modules
- Shadow Parts - expose parts of the shadow DOM to the parent DOM tree az *pseudo-elements*
- Declarative Shadow DOM - fill the shadow DOM from a template w/o using any JS
