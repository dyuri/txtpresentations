# Cross-Origin Resource Sharing

Modern browsers apply the *same-origin policy* to some resources, meaning they refuse to load or
restrict access to resources coming from other origins than the loaded website.
Servers can implement **CORS** to describe which origins are permitted to load their resources.

For some HTTP requests, browsers issue a "preflight" request (HTTP OPTIONS) to check whether
the resource is available for the given origin.

## Requests using CORS

- `XMLHttpRequest` or `fetch()`
- web fonts
- WebGL textures
- Images/videos drawn to canvas using `drawImage()`

### Simple requests

Simple requests don't trigger preflight.

A request is a simple request if it meets all the following crireria:

- Methods: *GET*, *HEAD*, *POST*
- Only extra headers allowed:
  - `Accept`
  - `Accept-Language`
  - `Content-Language`
  - `Content-Type` *(not all)*
- Allowed *Content-Type* values (backward compatibility):
  - `application/x-www-form-urlencoded`
  - `multipart/form-data`
  - `text/plain`

Browsers issue these kind of simple requests without preflight, and process their `Access-Control-*` headers.

### Requests with preflight

Before sending requests (that doesn't meet the criteria above) to an other origin, browsers issue a *preflight* request to check if the server allows it.

The preflight is an HTTP OPTIONS call with the following headers:

- `Origin`
- `Access-Control-Request-Method`
- `Access-Control-Request-Headers`

### Credentials

By default, `XMLHttpRequest` and `fetch()` does not send HTTP cookies with cross-origin requests. It's possible to include those with the `withCredentials` parameter, but the server needs to respond with `Access-Control-Allow-Credentials: true` otherwise the browser will drop the response.

The wildcard `Access-Control-Allow-Origin: *` cannot be used with credentials.

### Response headers

- `Access-Control-Allow-Origin` - explicit origin or `*`
- `Access-Control-Expose-Headers` - the listed headers will be exposed to the browser
- `Access-Control-Max-Age` - the time in seconds the preflight request can be cached.
- `Access-Control-Allow-Credentials` 
- `Access-Control-Allow-Methods`
- `Access-Control-Allow-Headers`

### Security

CORS only protects clients that implements it properly - browsers -, does not protect the backend from bots and such.
