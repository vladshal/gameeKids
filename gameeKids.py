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
    mc.setBlocks(0,0,0,15,0,15,block.GRASS)
    mc.setBlocks(-1,0,16,16,5,16,block.MOSS_STONE)
    mc.setBlocks(16,0,-1,16,5,16,block.MOSS_STONE)
    mc.setBlocks(-1,0,-1,-1,5,16,block.MOSS_STONE)
    mc.setBlocks(0,0,-1,15,5,-1,block.MOSS_STONE)
    
    mc.setBlocks(0,-5,0,15,-5,15,block.WOOD_PLANKS)
    mc.setBlocks(-1,-5,16,16,0,16,block.BOOKSHELF)
    mc.setBlocks(16,-5,-1,16,0,16,block.BOOKSHELF)
    mc.setBlocks(-1,-5,-1,-1,0,16,block.BOOKSHELF)
    mc.setBlocks(0,-5,-1,15,0,-1,block.BOOKSHELF)
    
    mc.setBlocks(0,-10,0,15,-10,15,block.WOOL)
    mc.setBlocks(-1,-10,16,16,-5,16,block.BRICK_BLOCK)
    mc.setBlocks(16,-10,-1,16,-5,16,block.BRICK_BLOCK)
    mc.setBlocks(-1,-10,-1,-1,-5,16,block.BRICK_BLOCK)
    mc.setBlocks(0,-10,-1,15,-5,-1,block.BRICK_BLOCK)

    mc.setBlocks(0,-15,0,15,-15,15,block.SNOW)
    mc.setBlocks(-1,-15,16,16,-10,16,block.ICE)
    mc.setBlocks(16,-15,-1,16,-10,16,block.ICE)
    mc.setBlocks(-1,-15,-1,-1,-10,16,block.ICE)
    mc.setBlocks(0,-15,-1,15,-10,-1,block.ICE)

    mc.setBlocks(0,-15,0,15,-15,15,block.GLOWING_OBSIDIAN)
    mc.setBlocks(-1,-15,16,16,-10,16,block.LAVA)
    mc.setBlocks(16,-15,-1,16,-10,16,block.LAVA)
    mc.setBlocks(-1,-15,-1,-1,-10,16,block.LAVA)
    mc.setBlocks(0,-15,-1,15,-10,-1,block.LAVA)
    
    mc.setBlocks(0,-20,0,15,-20,15,block.STONE)
    mc.setBlocks(-1,-20,16,16,-15,16,block.DIAMOND_ORE)
    mc.setBlocks(16,-20,-1,16,-15,16,block.GOLD_ORE)
    mc.setBlocks(-1,-20,-1,-1,-15,16,block.IRON_ORE )
    mc.setBlocks(0,-20,-1,15,-15,-1,block.REDSTONE_ORE)
    
def game():
    b = mc.player.getPos()
    sleep(0.2)   
    mc.setBlock(b.x,b.y-1,b.z,block.AIR)   
def main():
    prepare()
    while True:
        game()
    
main()
    
    


