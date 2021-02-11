# Rendering data to HTML

- offline/static
- online/dynamic

## Offline

Somebody or something generates the raw HTML "offline", long before the request, then the generated HTML is served via a static webserver (nginx, apache, ...) or CDN.

### How to create?

- via text editor
- static site generators

*Jamstack* is quite trendy nowadays.

#### Pros/cons

- quick as hell - markup is immediately available for the browser
- *eco friendly* - minimal power consumption during serving

- every visitor gets the same content
- changing anything might require lot of work (for you or for the site generator)

## Online

The HTML content is generated when the visitor requests it.

### Classic backend rendering

The more *classic* solution, something running on the backend side generates HTML for the visitor. CGI-BIN, PHP, Java servlet (JSP), etc.

It's most probably some kind of fancy string concatenation, but that's OK.

#### Pros/Cons

- different visitors might get different content
- serving dynamically generated content is much slower than static one (even using extensive caching)
- once generated and served, the markup is immediately available for the browser to parse / render

### Frontend rendering

A skeleton website and a *heavy* JS application is served initially, which then renders the HTML content using API calls.

SPAs / PWAs.

#### Pros/Cons

- markup is generated in the browser
- very quick in-site navigation
  - API call only for the data
  - even DOM elements can be reused (vDOM, other smart tricks)
- first load can be very slow
  - partial bundling
  - service workers, extensive frontend caching

## Mix them as you need

But carefully, you can speed things up but also slow them down, there's no ultimate solution.

### Example scenarios (notes)

**#1 SPA backend render**

- React SPA takes too much time to load for the first time
- move rendering to dynamic backend using nodejs without changing much
- performance gets even worse
- ?
  - React uses vDOM for rendering, it might help in the browser, but has no benefit - and slower than simple template rendering - on the backend
  - backend performs the same API calls - they might take less time, but still
  - the application still needs to get to the frontend - the rendered HTML w/o the JS app will do nothing (it can be displayed earlier, but in a *dummy* state)

**#2 pre-rendered webshop**

- static pages are generated via CMS content
- customer (cart, ordering) related stuff are handled via lightweight JS app + API calls



**TODO**

- hol mihez fer hozza (adat, eroforras)
- webcomponents?