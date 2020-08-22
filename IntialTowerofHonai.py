# create Method

def drawPole():
    for x in range(1,5,1):
        print ("      |")
        
def drawBase():
    print('----------')

def drawTitle(title):
    print(f"     {title}")
    
def drawTower(title):
    drawPole()
    drawBase( )
    drawTitle(title)
    
drawTower("Tower-A")
drawTower("Tower-B")    
drawTower("Tower-C")       