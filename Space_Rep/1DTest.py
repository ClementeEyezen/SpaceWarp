from Map import Map
from Map import Coordinate

def main():
    c1 = Coordinate(0,0,0)
    c2 = Coordinate(10,10,10)
    m = Map()
    carl = m.map_1D_space(c1,c2,5)

    for index, item in enumerate(carl):
        print str(index)+' '+str(item.x)+' '+str(item.y)+' '+str(item.z)
    
if __name__ == '__main__':
    main()