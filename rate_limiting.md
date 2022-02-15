# Rate limiting

## Why?

- DoS - Denial of Service attacks

- Brute Force attacks
  
  - collect customer email addresses (signup)
  
  - reveal username/password pairs (login)
  
  - send emails (contact us, gift card)

## How?

Really hard to do it properly.

- Session based: creating a new session is easy

- IP based
  
  - easy to get lot of IP addresses
  
  - might restrict real users behind NAT/IPv6 gateway

- Captcha (classic) - bad UX

- slow down API response artificially - can lead to "self-DoS"

## Knocking

Before calling a protected API, the client should *knock* calling a special knocking API with the target endpoint. The knocking API returns a waiting time after the target API will be available for one call.

Using some kind of classifier (Google reCAPTCHA v3, something based on user history, ...) the waiting time can be different for each user.

Calling a protected API requires the client to:

- create and maintain a session (bots usually don't do this)

- call the knocking API

- process the response, wait for the waiting time

- call the actual API

- (repeat the whole process)

Rejecting an API call (before the end of the waiting time or without calling the knocking API) is quick and easy, without using much backend resources. (HTTP 429 - Too Many Requests)
