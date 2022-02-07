# Cross-Site Request Forgery

CSRF is an attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated.

### Examples

**GET**

In FD, a "malcious" website can change the customers express status. This is at most annoying, clearly visible for the customer, and does not happen during a typical FD session, but if the request could change something import, it could be dangerous.

```html
<!-- https://whatever.com/express.html -->
<h1>not at all malcious site</h1>
<img src="https://www.freshdirect.com/index.jsp?expressContext=true" style="width: 1px; height: 1px;">
```

Upon visiting this website, the URL in the `img` tag will be called, with the proper cookies, and the customer will have express context enabled.

*GET* requests in general should not change any important state at the backend side.

**POST**

Imagine an internet banking website, that has a classic HTML `form` for money transfer. Without CSRF protection, an attacker could create a site from where they can POST data to the banking site:

```html
<!-- https://jedi.name/ -->
<h1>enter your favourite color, and I'll tell you your jedi name!</h1>
<form action="https://nocsrf-banking.com/transfer">
  <input name="color" placeholder="favourite color" value="">
  <input type="hidden" name="recipient" value="[haxoraccountnumber]">
  <input type="hidden" name="amount" value="$1000">
  <button>SHOW ME MY JEDI NAME!</button>
</form>
```

If the victim used the banking site recently and their session is still live, entering anything into that form and submitting it would transfer $1000 to the attacker.

## Mitigation

#### CSRF tokens

Tokens (generated once per session or for each request) are generated at the backend, sent to the frontend, and should be included for all state changing requests. The backend should deny the request if the token validation fails.

CSRF tokens should be:

- unique per session (or request)

- secret

- unpredictable (random)

They should not be transmitted from the frontend via `cookies`, but in a hidden form field (classic forms) or in a custom HTTP header (JS).

#### SameSite cookie attribute

If the session cookie is protected by the `SameSite` attribute (using `Strict` or `Lax` value), the cookie will not be included in cross-site requests (or only for *safe* requests in case of `Lax` - safe requests should not modify state, like `GET` or`HEAD`)

This attribute should not be the only protection, but an extra layer.

If we need to support cross-origin requests with credentials, we cannot use this.

#### Verifying standard headers

The backend can verify the `Origin` or the `Referer` header to check whether the request is a cross-origin, or same-site request. These headers are not always included, aren't really reliable.

(Browsers does something similar for CORS. See [cors.md](cors.md).

#### Custom header for AJAX

Only a few request headers can be set for an AJAX call without involving CORS, so setting one (and checking it in the backend side) will protect these API endpoints against CSRF.
