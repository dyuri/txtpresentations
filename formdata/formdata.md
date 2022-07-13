# Form data

How form data can get from the browser to the backend.

## Without JS

- `action`: where to send the data (URL, current URL by default)
- `method`: `GET`, `POST` (and there's `dialog` too...)
- `enctype`: only for `POST`, `Content-Type` of the data
  - `application/x-www-form-urlencoded` - default, URL encoded body
  - `multipart/form-data` - multipart data, required for file uploads
  - `text/plain` - for debugging, don't use, security issues

## With JS

`FormData` API - serializes form data for `fetch()` or `XMLHttpRequest.send()`

Example:

```javascript
let data = new FormData(document.getElementById("myform"));
fetch("/api/posthere", {
  method: "POST",
  body: data
});
```

- `Content-Type` automatically set to `multipart/form-data` (can be overridden, but don't!)
- files are handled automatically
- extra data can be `.append()`-ed, or unused `.delete()`-ed

To send `application/x-www-form-urlencoded` (which is the default for HTML forms) you can use `URLSearchParams` to convert `FormData` to URL encoded searchparams format. (Files won't work.)

```javascript
let formdata = new FormData(document.getElementById("myform"));
let data = new URLSearchParams(formdata);
fetch("/api/posthere", {
  method: "POST",
  body: data
});
```

`FormData` can be easily converted to JSON as well. In this case, `Content-Type` header must be explicitly set to `application/json`.

```javascript

let formdata = new FormData(document.getElementById("myform"));
let plaindata = Object.fromEntries(formdata.entries());
let data = JSON.stringify(plaindata);
fetch("/api/posthere", {
  method: "POST",
  hearders: {
    "Content-Type": "application/json"
  },
  body: data
});
```

# TODO: toDataURL, toBlob
