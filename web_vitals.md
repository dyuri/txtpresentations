# Core Web Vitals

Google: "page experience" will be (June 2021) part of search ranking

## What

- LCP: Largest Contentful Paint
- FID: First Input Delay (RUM only)
- CLS: Cumulative Layout Shift

Other (also important) metrics, abbreviations:

- TTFB: Time To First Byte - request sent => the first byte arrives (basically backend)
- FP: First Paint - anything rendered (except background color)
- FCP: First Contentful Paint - something that is "contentful" is rendered
  - has visible text
  - image, canvas, video
  - input w/ non-empty value
- TTI: Time To Interactive - page is loaded, event handlers registered, reacts within 50ms
- TBP: Total Blocking Time - FCP => TTI (main thread is blocked by initializing scripts)
- Lab metrics: you can measure them via tools
- RUM: Real User Metrics - you cannot measure them via tools :)
  - available through CrUX (Chrome User Experience Report)

### LCP

Like FCP, but not for the first, but the largest ("most interesting") element in the page.

### FID

Time between interaction (click) and response (navigation, xhr, overlay opening, whatever). Basically the time the event listeners take to run.

### CLS

Visual stability of the page. When the page "jumps" it's bad UX - late loading ads, jumpy menus/dropdowns, ... and it's measured throughout the life of the page.

### RUM

Real user metrics means that the website will be measured by its real visitors using various hardware (mobile, desktop, tv, refrigerator, ...), software (basically just Chrome, but different versions on various OS-es) and network connection (from fiber to 2G mobile).

LCP is most probably network related, FID depends on the CPU, and CLS might be affected by ad blockers and user behavior.