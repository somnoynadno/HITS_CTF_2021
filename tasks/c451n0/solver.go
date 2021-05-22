package main

import (
    "bufio"
    "fmt"
    "log"
    "net"
    "regexp"
    "strconv"
    "strings"
    "time"
)

func rand(x int) int {
    return (((x + 12345) * 678) % 123456789) % 37
}

func main() {
    var results []int
    re := regexp.MustCompile("[0-9]+")

    seed := int(time.Now().Unix())

    conn, err := net.Dial("tcp", "somnoynadno.ru:10009")
    if err != nil {
        log.Println(err)
        return
    }
    defer conn.Close()

    balance := 100

    scanner := bufio.NewScanner(conn)

    for scanner.Scan() {
        message := scanner.Text()
        message = strings.TrimSpace(message)
        message = strings.Trim(message, "\n")
        fmt.Println(message)

        if message == "Place the bets!" {
            , err := conn.Write([]byte(strconv.Itoa(rand(seed)) + "\n"))
            if err != nil {
                log.Println(err)
            }
        } else if message == "How much you wanna place?" {
            , err := conn.Write([]byte(strconv.Itoa(balance) + "\n"))
            if err != nil {
                log.Println(err)
            }
        } else if strings.Contains(message, "It's ") {
            balance *= 10
            resultRaw := re.FindString(message)
            result, _ := strconv.Atoi(resultRaw)
            results = append(results, result)

            seed += result
        }
    }
}
