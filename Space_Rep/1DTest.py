from Map import Map
from Map import Coordinate

def main():
    print ("Main called")
    c1 = Coordinate(0,0,0)
    c2 = Coordinate(10,10,10)
    m = Map()
    print ("begin mapping")
    carl = m.map_1D_space(c1,c2,5)
    print ("endin mapping")
    for index, item in enumerate(carl):
        print (''+str(index)+' '+str(item.coordinate.x)+' '+str(item.coordinate.y)+' '+str(item.coordinate.z))
    
if __name__ == '__main__':
    main()