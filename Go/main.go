package main

import (
	"fmt" // Standard Go package
	"io/ioutil" // I/O utility functions
	m "math" // Maths library, local alias is "m"
	"net/http" // Web server library
	"os" // Library for navigating the OS' filesystem
	"strconv" // String conversion library
)
// Simple Hello World script, nothing to see here
func main() {
	fmt.println("Hello World!")

	beyondHelloWorld()
}

func beyondHelloWorld() {
	var x int // Declares a variable exists, but doesn't assign it a value
	x = 3 // Great! Now we've given the variable 'x' the value of 3
	y := 4 // By declaring a variable like this, it declares the variable while simultaneously assigning it a value

	learnVarTypes()
}

func learnVarTypes() {
	str := "This program was written in Go!" // This variable is a string

	s2 := `This is a "raw" string, which allows line
breaks`

	g := "∑" // Runes, alias for int32, and holds a unicode code point

	f := 3.14195 // Float, or float64, a 64-bit floating point number
	c := 3 + 4i // Complex128, internally represented by 2 float64s
}
