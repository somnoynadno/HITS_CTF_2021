package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"github.com/google/uuid"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

var API = "http://evilinsult.com/generate_insult.php?lang=en&type=json"

var PORT = os.Getenv("PORT")

var FLAG1 = os.Getenv("FLAG1")
var FLAG2 = os.Getenv("FLAG2")

var DIR = "/tmp"

type SecretBody struct {
	UserUUID     string
	ServerSecret string
}

func GetInsult(w http.ResponseWriter, req *http.Request) {
	id := uuid.New().String()
	go sendRequest(id)

	message := "Your insult is available at /insult?id=" + id
	_, _ = fmt.Fprint(w, message)
}

func sendRequest(id string) {
	filename := DIR + "/" + id

	sb := SecretBody{ServerSecret: FLAG2, UserUUID: id}
	b, _ := json.Marshal(sb)

	err := ioutil.WriteFile(filename, b, 0644)
	if err != nil {
		log.Println(err)
		return
	}

	res, err := http.Post(API, "application/json", bytes.NewBuffer(b))
	if err != nil {
		log.Println(err)
		return
	}

	responseData, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Println(err)
		return
	}

	err = ioutil.WriteFile(filename, responseData, 0644)
	if err != nil {
		log.Println(err)
		return
	}
}

func ShowInsult(w http.ResponseWriter, req *http.Request) {
	id := req.URL.Query().Get("id")
	filename := DIR + "/" + id

	data, err := ioutil.ReadFile(filename)
	if err != nil {
		handleError(w, err)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	_, _ = fmt.Fprint(w, string(data))
}

func handleError(w http.ResponseWriter, err error) {
	log.Println(err)
	http.Error(w, err.Error(), http.StatusInternalServerError)
}

func init() {
	err := ioutil.WriteFile("/secret/flag.txt", []byte(FLAG1), 0644)
	if err != nil {
		panic(err)
	}
}

func main() {
	http.HandleFunc("/", GetInsult)
	http.HandleFunc("/insult", ShowInsult)

	if PORT == "" {
		PORT = "8080"
	}

	log.Println("Listening on: " + PORT)
	err := http.ListenAndServe(":"+PORT, nil)
	if err != nil {
		panic(err)
	}
}
