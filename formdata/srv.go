package main

import (
	"bytes"
	"fmt"
	"html/template"
	"net/http"
)

func posthandler(w http.ResponseWriter, r *http.Request) {
	tmpl := template.Must(template.ParseFiles("html/index.html"))

	buf := new(bytes.Buffer)
	buf.ReadFrom(r.Body)
	body := buf.String()

	tmpl.Execute(w, body)
}

func apiposthandler(w http.ResponseWriter, r *http.Request) {
	buf := new(bytes.Buffer)
	buf.ReadFrom(r.Body)
	body := buf.String()

	fmt.Fprint(w, body)
}

func main() {
	http.HandleFunc("/", posthandler)
	http.HandleFunc("/api", apiposthandler)

	fmt.Println("Listening on http://localhost:8765/")
	http.ListenAndServe(":8765", nil)
}
