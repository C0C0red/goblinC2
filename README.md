# goblinC2
<div>
    <img src="https://img.shields.io/badge/-Linux-grey?logo=Linux&logoColor=white" width="65px">
    <img src="https://img.shields.io/badge/-Windows-blue?logo=Windows&logoColor=white" width="90px">
    <img src="https://img.shields.io/badge/-Go-blue?logo=Go&logoColor=white" width="50px">
    <img src="https://img.shields.io/badge/-Python3-3776AB?logo=Python&logoColor=white" width="85px">
</div>

---


## ▪️ Check the video
[**Demo Video**](https://youtu.be/ajL3QlP7ypA)

---
## ▪️ You will need 
- [**Python3**](https://www.python.org/downloads/)
- [**Golang**](https://go.dev/dl/)

---
## ▪️ Install
```
mkdir ~/goblin ; cd ~/goblin ; wget https://raw.githubusercontent.com/h0ru/goblinC2/main/server/goblin.py . ; chmod +x ./goblin.py ; wget https://raw.githubusercontent.com/h0ru/goblinC2/main/client/lin.go . ; wget https://raw.githubusercontent.com/h0ru/goblinC2/main/client/win.go . ; wget https://raw.githubusercontent.com/h0ru/goblinC2/main/client/lin.py
```
---
## ▪️ Help
- **ModuleNotFoundError: No module named 'prettytable'**
```
pip install prettytable
```
- **Compile your Linux and Windows clients with a different name**
```
GOOS=linux GOARCH=amd64 go build -o name lin.go
GOOS=windows GOARCH=amd64 go build -o name.exe win.go
```
- **Menu Commands**
```
help or ?                   ~> Show Help Menu
exit or x                   ~> Exits C2
listener or lt              ~> Generate a New Listener
lin                         ~> Generate a Linux Payload
win                         ~> Generate a Windows Payload
sessions -l                 ~> List Sessions
sessions -i <id>            ~> Enter a New Session
```
- **Sessions Commands**
```
help or ?                   ~> Show Help Menu
exit or x                   ~> Terminates the current session
persist or pt               ~> Use a persistence technique
background or bg            ~> Backgrounds the current session
```
- **Compilation Warning: GLIBC_2.34 Compatibility Issue**
  - Try Compiling [lin.go](https://github.com/h0ru/goblinC2/blob/main/client/lin.go) in a Specific Environment: If you're facing compatibility problems due to GLIBC version differences, attempt to compile the lin.go source code in an environment that matches your target system's GLIBC version. This might help create a binary that's compatible with your desired environment.

  - Alternatively, Use [lin.py](https://github.com/h0ru/goblinC2/blob/main/client/lin.py) as an Option: In case you're still encountering challenges with Go's compatibility, you can explore the alternative lin.py script. This Python script might offer a workaround for executing the desired functionality on systems with varying GLIBC versions.
   - Remember to update the fields:
```
host_ip = 'INPUT_IP_HERE'
host_port = INPUT_PORT_HERE
```
---

