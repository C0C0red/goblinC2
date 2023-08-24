# goblinC2
<div>
    <img src="https://img.shields.io/badge/-Linux-grey?logo=Linux&logoColor=white" width="65px">
    <img src="https://img.shields.io/badge/-Windows-blue?logo=Windows&logoColor=white" width="90px">
    <img src="https://img.shields.io/badge/-Go-blue?logo=Go&logoColor=white" width="50px">
    <img src="https://img.shields.io/badge/-Python3-3776AB?logo=Python&logoColor=white" width="85px">
</div>

## ▪️ You will need 
- [**Python3**](https://www.python.org/downloads/)
- [**Golang**](https://go.dev/dl/)

---
## ▪️ Install
```
mkdir ~/goblin ; cd ~/goblin ; wget https://raw.githubusercontent.com/h0ru/goblinC2/main/server/goblin.py . ; chmod +x ./goblin.py ; wget https://raw.githubusercontent.com/h0ru/goblinC2/main/client/lin.go . ; wget https://raw.githubusercontent.com/h0ru/goblinC2/main/client/win.go .
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
---

