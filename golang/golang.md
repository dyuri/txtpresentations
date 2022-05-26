# Go(lang)

## What?

- statically typed (w/ type inference)
- compiled (statically linked)
- memory safety, garbage collection
- built in dependency management
- concurrency:
  - goroutines (~coroutines/threads)
  - channels
  - select (for channels)
- interfaces for "virtual inheritance", type embedding
- standardized formatting (gofmt)
- multiple implementations (gc, gccgo, gollvm, gopherjs, ...)

## Why?

- mascot: **go**pher
- started by **Go**ogle in 2007
- focusing on multicored/networked problems
- efficient (like C)
- readable & usable (like Python)
- high performance networking & multiprocessing
- primary motivation: dislike of C++ :)

## How?

Play with it: [Go Playground](https://go.dev/play/)

### Flow control

#### for

Classic:

```go
for i := 0; i < 10; i++ {
    fmt.Println(i)
}
```

*While*:

```go
sum := 0
for sum < 100 {
    sum += 1
}
```

Endless loop:

```go
for {
    // neverending story
}
```

#### if

```go
if i < 10 {
    // i < 10
} else {
    // i >= 10
}
```

W/ short statement:

```go
if s := math.Sin(f); s < .5 {
    return s
}
// s isn't defined here
```

#### switch

Basically many `if`s, no silly `break`s and such:

```go
switch os := runtime.GOOS; os {
case "darwin":
    // MacOS
case "linux":
    // Linux
default:
    // anything else
}
```

#### defer

Defers execution until the function returns (~finally).

```go
func x(i) {
    defer fmt.Println("x exited")

    if i > 10 {
        return "big"
    }
    return "small"
}
```

Deferred functions are stacked, called in a reverse order.

### Types

No variable is *uninitialized*.

#### Basic types, zero values

- bool (false)
- numbers (byte, uint8, int16, float32, complex128, ...) (0)
- string ("")
- rune (int32 - unicode character) ('')

Inference:

```go
var i int // i == 0
j := 16 // j is int
k := i + j // k is 16, int
```

#### Pointers, references

Without pointer arithmetic:

```go
i := 42
p = &i
*p = 21
fmt.Println(*p) // prints 21
```

#### Structs

```go
type Color struct {
    R, G, B int
    Alpha float32
}

c1 := Color{100, 200, 200, .5}
c.R = 200 // {200, 200, 200}
```

#### Arrays

```go
var a [2]int
a[0] = "Hello"
a[1] = "World"

nums := [4]int{1,2,3,4}
```

#### Slices

~*dynamic views* of arrays

```go
nums2 := nums[1:3] // {2, 3}, nums2 is a slice, not an array
nums2[0] := 5 // nums became {1,5,3,4}

nums3 := []int{5,4,3,2,1} // nums3 is a slice, the underlying array is hidder
```

- length - current size of the view
- capacity - the size of the underlying array
- `make()` - create slice with the given length/capacity
- `append()`- *smart* append, increases capacity when required
- `range` - for iterating through iterables

```go
nums4 := make([]int, 1, 2) // {0} with capacity of 2
nums4[:cap(num4)] // {0, 0}
append(nums4, 1, 2, 3) // {0, 0, 1, 2, 3}, no idea of capacity, maybe 8

for i, v := range nums4 {
    fmt.Printf("%d. %d\n", i, v)
}
```

#### Maps

Nothing special, `make` can also used to create them.

```go
var m1 map[string]int
m1["cica"] = 4
m1["kutya"] = 27


m2 := map[string]int{
    "cica": 5,
    "kutya": 28,
}

m3 := make(map[string]int)

// check if key is included
v1, ok := m1["egér"] // v1 == 0, ok == false
```

#### Functions

... can be values too.

```go
func add(x, y int) int {
    return x + y
}

func applyWith2(x int, fn func(int, int) int) int {
    return fn(x, 2)
}
```

Error handling: return it!

```go
func div(x, y int) (int, error) {
    if y == 0 {
        return 0, errors.New("Cannot divide by zero!")
    }
    return x / y, nil
}
```

Parameters are passed as *value* by default, so copyed on function call - but you can explicitly use pointers to avoid copying or to be able to modify the original object.

### Methods

Go does not have classes, but you can define methods on types - not just structs, but any type defined in the same package. They are basically functions, with a *receiver* argument.

```go
type Color struct {
    R int `json:"red"` // example for tags
    G int `json:"green"`
    B int `json:"blue"`
}

func (c Color) Grayscale() Color {
    g := (c.R + c.G + c.B) / 3
    return Color{g, g, g}    
}

func (c *Color) Darken() { // can use pointers as well
    c.R = c.R / 2
    c.G = c.G / 2
    c.B = c.B / 2
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }

    return float64(f)
}
```

### Interfaces

Interface: a set of method signatures.

```go
type Abser interface {
    Abs() float64
}

func PrintAbs(a Abser) {
    fmt.Println(a.Abs())
}

// PrintAbs(MyFloat(-12))
```

Implementation is *implicit*, `MyFloat` is an `Abser`, even if I defined the interface later (even in an other package).

Special *empty interface*: `interface{}`- all types implement it, ~`Object`.

Type assertion:

```go
func PrintAbs(a Abser) {
    i, ok := a.(MyInt)
    if ok {
        // handle integer
    }

    f, ok := a.(MyFloat)
    if ok {
        // handle float
    }

    // OR

    switch v := i.(type) {
    case MyInt:
        // handle MyInt
    case MyFloat:
        // handle MyFloat
    default:
        // whatever
    }
}
```

Interface example: `fmt.Stringer`-> anything w/ a`String()`method

`error` is an interface too:

```go
type error interface { // this is built in
    Error() string
}

type MyError struct {
    When time.Time
    What string
}

func (e *MyError) Error() string {
    return fmt.Sprintf("[%v] %s", e.When, e.What)
}
```
