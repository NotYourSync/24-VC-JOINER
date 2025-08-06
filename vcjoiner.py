# MADE BY SYNCJIJA / SYNCROOT / SYNC
# DISCORD - https://discord.gg/SyMJymrV8x
# GITHUB - https://github.com/NotYourSync
# VC JOINER 24/7 MULTI TOKENS
# DO NOT SKID.

import asyncio as asyncdevelopment
import aiohttp
import websockets
import json as syncjijaxrootsync
import os as syncpapa
import ssl
from colorama import init, Fore

init(autoreset=True)

def syncjija():
    syncpapa.system('cls' if syncpapa.name == 'nt' else 'clear')

def papasync():
    print(Fore.CYAN + r"""
██▒   █▓ ▄████▄      ▄▄▄██▀▀▀▒█████   ██▓ ███▄    █ ▓█████  ██▀███
▓██░   █▒▒██▀ ▀█        ▒██  ▒██▒  ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
 ▓██  █▒░▒▓█    ▄       ░██  ▒██░  ██▒▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
  ▒██ █░░▒▓▓▄ ▄██▒   ▓██▄██▓ ▒██   ██░░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄
   ▒▀█░  ▒ ▓███▀ ░    ▓███▒  ░ ████▓▒░░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
   ░ ▐░  ░ ░▒ ▒  ░    ▒▓▒▒░  ░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
   ░ ░░    ░  ▒       ▒ ░▒░    ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
     ░░  ░            ░ ░ ░  ░ ░ ░ ▒   ▒ ░   ░   ░ ░    ░     ░░   ░
      ░  ░ ░          ░   ░      ░ ░   ░           ░    ░  ░   ░
     ░
    """)

    print(Fore.MAGENTA + "\n╔════════════════════════════════════════════════════════════╗")
    print(Fore.MAGENTA + "║" + Fore.CYAN + "               24/7 Multi Token VC Joiner By $ync             " + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "╠════════════════════════════════════════════════════════════╣")
    print(Fore.MAGENTA + "║" + Fore.GREEN + " Discord:" + Fore.WHITE + " https://discord.gg/SyMJymrV8x                    " + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "║" + Fore.GREEN + " GitHub :" + Fore.WHITE + " https://github.com/NotYourSync                   " + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "╚════════════════════════════════════════════════════════════╝\n")

def configproxy():
    path = 'config.sync'
    if not syncpapa.path.exists(path):
        config = {
            "tokens": [],
            "guild_id": "",
            "channel_id": "",
            "voice_settings": {
                "self_mute": False,
                "self_deaf": True
            }
        }
        with open(path, 'w') as f:
            syncjijaxrootsync.dump(config, f, indent=4)
        return config
    with open(path, 'r') as f:
        return syncjijaxrootsync.load(f)

def inputdata(config):
    if not config['tokens']:
        config['tokens'] = [input("Enter your user token: ").strip()]
    if not config['guild_id']:
        config['guild_id'] = input("Enter Guild ID: ").strip()
    if not config['channel_id']:
        config['channel_id'] = input("Enter Voice Channel ID: ").strip()
    with open('config.sync', 'w') as f:
        syncjijaxrootsync.dump(config, f, indent=4)
    return config

async def heartbeat(ws, interval):
    try:
        while True:
            await asyncdevelopment.sleep(interval / 1000)
            await ws.send(syncjijaxrootsync.dumps({"op": 1, "d": None}))
    except:
        pass

async def vconnect(token, config):
    ws_url = "wss://gateway.discord.gg/?v=9&encoding=json"
    ssl_ctx = ssl.create_default_context()

    while True:
        try:
            print(Fore.CYAN + f"[Connecting] Token ending in: {token[-6:]}")
            async with websockets.connect(ws_url, ssl=ssl_ctx) as ws:
                hello = syncjijaxrootsync.loads(await ws.recv())
                asyncdevelopment.create_task(heartbeat(ws, hello['d']['heartbeat_interval']))

                await ws.send(syncjijaxrootsync.dumps({
                    "op": 2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": "linux",
                            "$browser": "chrome",
                            "$device": "pc"
                        },
                        "compress": False
                    }
                }))

                while True:
                    msg = await ws.recv()
                    event = syncjijaxrootsync.loads(msg)
                    if event.get('t') == 'READY':
                        print(Fore.GREEN + f"[Logged in as] {event['d']['user']['username']}")
                        await ws.send(syncjijaxrootsync.dumps({
                            "op": 4,
                            "d": {
                                "guild_id": config['guild_id'],
                                "channel_id": config['channel_id'],
                                "self_mute": config['voice_settings']['self_mute'],
                                "self_deaf": config['voice_settings']['self_deaf']
                            }
                        }))
                        print(Fore.GREEN + f"[Joined VC] {config['channel_id']}")
        except Exception as e:
            print(Fore.RED + f"[Error] {str(e)}")
        await asyncdevelopment.sleep(5)

async def main():
    syncjija()
    papasync()
    config = configproxy()
    config = inputdata(config)

    tokens = config.get('tokens', [])
    if not tokens:
        print(Fore.RED + "No tokens found.")
        return

    print(Fore.BLUE + "[Starting] No Proxy Multi Token VC Joiner...\n")
    tasks = [vconnect(token, config) for token in tokens]
    await asyncdevelopment.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncdevelopment.run(main())
    except KeyboardInterrupt:
        print(Fore.RED + "\n[Stopped by User]")
    except Exception as e:
        print(Fore.RED + f"[Fatal Error] {e}")
        