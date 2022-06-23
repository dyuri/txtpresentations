# Go(lang) - advanced topics

## Concurrency

### Goroutines

Goroutine: a *lightweight thread* managed by the Go runtime.

It's pretty simple to execute a function call as a new goroutine:

```go
go f(param1, param2)
```

The program is terminated when the main goroutine finishes.

### Channels

Go `channel`s are typed *channels* through which you can send and receive values.

```go
ich := make(chan int)
// sending
ch <- 12
// receiving
v := <- ch
```

By default sends and receives are blocking until the other side reacts - this allows goroutines to synchronize without explicit locks and such.

Example:

```go
func sum(s []int, c chan int) {
    sum := 0
    for _, v := range s {
        sum += v
    }
    c <- sum // send through channel instead of return
}


func main() {
    s := []int{1, 2, 3, 4, 5, 6, 7, 8}
    
    c := make(chan int)
    go sum(s[:len(s)/2], c)
    go sum(s[len(s)/2:], c)
    x, y := <-c, <-c // receive two values through c
    
    fmt.Println(x+y)
}
```

Channels can be buffered:

```go
ch := make(chan int, 100)
```

Sends only block when the buffer is full, receives only when it's empty.

`range` supports channels (gives only the value), and `close()` can be used to close a channel.

```go
func fibo(n int, c chan int) {
    x, y := 0, 1
    for i := 0; i < n; i++ {
        c <- x
        x, y = y, x+y
    }
    close(c)
}

// ...
go fibo(10, ch)
for i := range ch {
    fmt.Println(i)
}

// can be checked too
nextfib, ok := <-ch
if ok != nil {
    fmt.Println("cannot read from channel, already closed?")
}
```

### Select

(**Note:** this isn't the `select()` unix system call!)

The `select` statement lets you wait on multiple channels. It blocks until one of it cases can run, then executes that one (chooses randomly if there are more).

```go
func fibo2(c chan int, quit chan bool) {
    x, y := 0, 1
    for {
        select {
        case c <- x: // send if you can
            x, y = y, y + x
        case <-quit: // quit if you're asked to
            fmt.Println("csá")
        }
    }
}


ch := make(chan int)
q := make(chan bool)
go func() {
    for i := 0; i < 10; i++ {
        fmt.Println(<-c)
    }
    quit <- true
}
fibo2(c, quit)
```

There's `default` for `select` as well, that you can use to implement non-blocking channel read:

```go
select {
case v <- ch:
    fmt.Println(v)
default:
    fmt.Println("channel empty")
}
```

### sync

The `sync` module contains various synchronization primitives to synchronize goroutines, like `sync.Mutex`, `sync.WaitGroup`, ...



## Generics

TODO...


