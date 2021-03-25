# Matrix

- 2019, https://matrix.org/
- not the movie, but the "matrixed communication"
- open standard: [spec](https://matrix.org/docs/spec/)
- non-profit Matrix.org Foundation
- decentralized
- end-to-end encryption
  - olm, megolm
  - based on Signal's [double ratchet](https://signal.org/docs/specifications/doubleratchet/)
  - extended to support encrypted rooms
- messaging (IM, rooms, bots, even IoT devices)
- signaling (for WebRTC, VoiP, video calls)
- bridging to other IM networks (XMPP, Slack, IRC, Discord, Facebook, ...)
- HTTPS+JSON based by default, but a much lighter UDP based demo was already created for ~100bps (!) networks

## How does it work?

- "decentralized message store"
- messages are replicated over all participating servers
- no single point control or failure
- more like e-mail than other IM protocols

## Who uses it?

- lot of clients (web, desktop, mobile, even console), client SDKs
- lot of bridges to other IM networks
- more than one server implementations
- free servers
- easy to self-host, easy to join the federation
- some numbers (matrix.org homeserver):
  - 10M+ accounts
  - 2.5M+ messages/day
  - 2.1M+ rooms
  - 20k+ federated servers
  - 400+ projects, 70+ companies building on Matrix
- "big" users
  - French Goverment
  - German Ministry of Defense
  - Mozilla
  - Gitter (chat for GitLab projects)