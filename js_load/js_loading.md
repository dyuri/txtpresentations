# Loading JS

## Different ways of static inclusion

![js load order](./js_loading.svg)
( (CC) whatwg.org )

## Loading JS from JS

### Classic way (works everywhere)

```javascript
function loadJS(src, cb) {
  const script = document.createElement("script");
  script.src = src;
  script.onload = cb;
  // script.async, script.defer, ... could be set here as well
  document.head.appendChild(script);
}

loadJS("/js/foobar.js", () => console.log("foobar loaded"));
```

#### Adding async/await

```javascript
const loadScript = async src => {
  return new Promise(resolve => {
    // loadJS from above, I don't want to copy it
    loadJS(src, () => resolve());
  });
};

// ! from an async context
await loadScript("/js/foobar.js");
console.log("foobar loaded");
```

### Modules

Modules can be loaded only from othen modules.

```javascript
import { whatever } from "foobar.js"; // cannot use variables here, and should be in the root context

whatever("hello");
```

#### Dynamic import

```javascript
const { whatever } = await import("foobar.js"); // variables can be used

whatever("hello");
```
