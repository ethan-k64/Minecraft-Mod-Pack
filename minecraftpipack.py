# Setup
from mcpi import minecraft
from mcpi import block
from time import sleep
import math

mc = minecraft.Minecraft.create()
mc.player.setting("autojump", False)
mc.setting("nametags_visible", True)

# Global Variables
air = 0
grass = 2
flower = 38
water = 8
water_source = 9
ice = 79
glowing_obsidian = 246
tnt = 46

option_1 = False
option_2 = False
option_3 = False
option_4 = False

custom = False

def console():
    global option_1
    global option_2
    global option_3
    global option_4
    global custom
    
    print("-=-=-=-=-");
    print("1) Auto Mine")
    print("2) Frost Walker")
    print("3) TNT Walker")
    print("4) Custom Walker")
    print("5) Save Game")
    print("6) Restore Game")
    print("7) Chat")
    print("8) Teleport")
    print("-=-=-=-=-");
    
    x = input("Enter an option: ")
    
    print("-=-=-=-=-");
    
    if x == "1":
        option_1 = True
        print("Running Auto Mine")
    elif x == "2":
        option_2 = True
        print("Running Frost Walker")
    elif x == "3":
        option_3 = True
        print("Running TNT Walker")
    elif x == "4":
        print("Enter the block ID: ")
        y = input()
        custom = int(y)
        option_4 = True
        print("-=-=-=-=-")
        print("Running Custom Walker")
    elif x == "5":
        print("Saving Game...")
        save()
    elif x == "6":
        print("Restoring Game...")
        restore()
    elif x == "7":
        z = input("Insert your message: ")
        chat(z)
    elif x == "8":
        tele_x = input("Enter the x coordinate: ")
        print("-=-=-=-=-")
        tele_y = input("Enter the y coordinate: ")
        print("-=-=-=-=-")
        tele_z = input("Enter the z coordinate: ")
        mc.player.setPos(tele_x, tele_y, tele_z)
    else:
        print("Enter a valid option")
        
    while option_1 == True:
        auto_mine()        
        
    while option_2 == True:
        frost_walker()
        
    while option_3 == True:
        destruction()
        
    while option_4 == True:
        custom_walker(custom)

def auto_mine():
    x, y, z = mc.player.getPos()
    
    mine = True

    if y - 1 < -63:
        mine = False
    else:
        mine = True
    
    if mine == True:
        mc.setBlock(x, y - 1, z, air)
        sleep(0.5)
        
def frost_walker():
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y - 1, z)

    if block_beneath == water_source or block_beneath == ice:
        mc.setBlock(x, round(y) - 1, z, ice)
        mc.setBlock(x - 1, round(y) - 1, z, ice)
        mc.setBlock(x + 1, round(y) - 1, z, ice)
        mc.setBlock(x, round(y) - 1, z - 1, ice)
        mc.setBlock(x, round(y) - 1, z + 1, ice)
        
        mc.setBlock(x - 2, round(y) - 1, z, ice)
        mc.setBlock(x + 2, round(y) - 1, z, ice)
        mc.setBlock(x, round(y) - 1, z - 2, ice)
        mc.setBlock(x, round(y) - 1, z + 2, ice)
        
        mc.setBlock(x - 3, round(y) - 1, z, ice)
        mc.setBlock(x + 3, round(y) - 1, z, ice)
        mc.setBlock(x, round(y) - 1, z - 3, ice)
        mc.setBlock(x, round(y) - 1, z + 3, ice)
        
        mc.setBlock(x - 1, round(y) - 1, z + 1, ice)
        mc.setBlock(x - 1, round(y) - 1, z - 1, ice)
        mc.setBlock(x + 1, round(y) - 1, z + 1, ice)
        mc.setBlock(x + 1, round(y) - 1, z - 1, ice)
        
        mc.setBlock(x - 1, round(y) - 1, z - 2, ice)
        mc.setBlock(x - 2, round(y) - 1, z - 1, ice)
        mc.setBlock(x + 1, round(y) - 1, z + 2, ice)
        mc.setBlock(x + 2, round(y) - 1, z + 1, ice)
        
        mc.setBlock(x - 1, round(y) - 1, z + 2, icss)
        mc.setBlock(x - 2, round(y) - 1, z + 1, ice)
        mc.setBlock(x + 1, round(y) - 1, z - 2, ice)
        mc.setBlock(x + 2, round(y) - 1, z - 1, ice)
        
def destruction():
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y - 1, z)
    
    if block_beneath != air:
        mc.setBlock(x, y - 1, z, tnt, 1)
        

def custom_walker(block):
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y - 1, z)
    
    if block_beneath != air:
        mc.setBlock(x, y - 1, z, block)

def save():
    mc.saveCheckpoint()
    
    
def restore():
    mc.restoreCheckpoint()
    
    
def chat(message):
    mc.postToChat(message)
    
# Loop
while True: 
    console()
    
