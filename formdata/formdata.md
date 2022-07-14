# Form data

How form data can get from the browser to the backend.

## Without JS

- `action`: where to send the data (URL, current URL by default)
- `method`: `GET`, `POST` (and there's `dialog` too...)
- `enctype`: only for `POST`, `Content-Type` of the data
  - `application/x-www-form-urlencoded` - default, URL encoded body
  - `multipart/form-data` - multipart data, required for file uploads
  - `text/plain` - for debugging, don't use, security issues

> Sidenote - MIME
> MIME: Multipurpose Internet Mail Extensions
> So mime types were basically invented for e-mails.

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

An image (or any other file) is basically binary data. We can embed binary data (almost) freely in a `multipart/form-data` message, but if we want to we can encode them somehow to be easily embedded into something that can handle only "strings" - like JSON. We might invent such an encoding, but fortunatelly there's already one standardized: the *data URL scheme*.

### Data URLs

`data:[<mediatype>][;base64],<data>`

- `data:` is the protocol (like `http:`)
- `mediatype` is the MIME type with charset and such (like `image/png` or `text/html;charset=utf-8`)
- `base64` means base64 encoding is used, if it's omitted, standard URL encoding should be used (`space` is `%20` for example)

The result is a URL, that can be used as a standard ASCII string, in a JSON message for example.

### ... adding *anything* to FormData

```javascript
formdata.append("image", data[, "filename.ext"]);
```

Data can be read from a canvas (`canvas.toDataURL()`, `canvas.toBlob()`), using the File API, or just by creating `Blob`s.
