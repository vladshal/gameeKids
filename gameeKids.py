import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Vec3
from minecraftstuff import MinecraftDrawing
from minecraftstuff import MinecraftShape, ShapeBlock
from random import randint
from time import sleep
mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)



def prepare():
    mc.setBlocks(0,0,0,15,0,15,block.TNT)
    mc.setBlocks(-1,0,16,16,5,16,block.BEDROCK)
    mc.setBlocks(16,0,-1,16,5,16,block.BEDROCK)
    mc.setBlocks(-1,0,-1,-1,5,16,block.BEDROCK)
    mc.setBlocks(0,0,-1,15,5,-1,block.BEDROCK)
def game():
    pass
        
def main():
    prepare()
    game()
    
main()
    
    


