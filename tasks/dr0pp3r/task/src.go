package main

import (
	"fmt"
)

func main() {
	// flag is HITS{un7r4c34bl3_3x3cu710n}
	flag := []int{72, 73, 84, 83, 123, 117, 110, 55, 114, 52, 99, 51, 52, 98, 108, 51, 95, 51, 120, 51, 99, 117, 55, 49, 48, 110, 125}
	gamma := []int{1, 2, 1, 3, 2, 0, 1, 3, 5, 2, 3, 1, 3, 1, 1, 2, 4, 3, 2, 1, 2, 2, 3, 1, 2, 3, 1}

	enc := ""
	for i := 0; i < len(flag); i++ {
		enc += string(rune(gamma[i] ^ flag[i]))
	}
	fmt.Println("Your encrypted flag is: " + enc)
}
