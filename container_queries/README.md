# Container queries

## The problem

Currently we have `media queries`, but in most cases widgets have not the full width of the viewport.

* [not responsive](example1.html)
* [responsive](example2.html)

## Partial solutions

Flexbox and grid layouts support some kind of *inner responsiveness*.

* [grid](example3.html)
* [flexbox](example4.html)

## `ResizeObserver` to the rescue

For more complex scenarios we have to use JavaScript currently. There are a lot of container query libraries, most of them overcomplicated to my taste. (One of the reasons why it is not yet in CSS.)

* [ResizeObserver](example5.html)
