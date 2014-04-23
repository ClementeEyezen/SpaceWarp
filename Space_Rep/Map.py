#quick changes for test

class Map(object):
    def __init__(self, space_constant = 1):
        global root
        root = LocatedNode(space_constant, Coordinate(0,0,0))
        global flex_constant
        flex_constant = space_constant
        global nodelist
        nodelist = []
        nodelist.append(root)
    def map_1D_space(self, start_coord, end_coord, resolution):
        # maps a line of nodes from coordinate to coordinate
        toReturn = []
        dx = (end_coord.val()[0]-start_coord.val()[0])/resolution
        dy = (end_coord.val()[1]-start_coord.val()[1])/resolution
        dz = (end_coord.val()[2]-start_coord.val()[2])/resolution
        step = 0
        while(step*dx<=(end_coord.val()[0]-start_coord.val()[0]) and step*dx<=(end_coord.val()[1]-start_coord.val()[1]) and step*dx<=(end_coord.val()[2]-start_coord.val()[2])):
            toReturn.append(LocatedNode(flex_constant, Coordinate(start_coord.val()[0]+step*dx, start_coord.val()[1]+step*dy, start_coord.val()[2]+step*dz )))
        return toReturn
        
        
    def map_2D_space(self, start_x, start_y, end_x, end_y, resolution):
        # maps a 2D grid of nodes from one coordinate to the other (opposite corners)
        # TODO
        pass
    def map_3D_space(self, start_coord, end_coord, resolution):
        # maps a 3D box of nodes from one coordinate to the other (opposite corners)
        # TODO
        pass

            
    def add_node(self, toAdd):
        if isinstance(toAdd, Node):
            connect_list = toAdd.get_connections()
            # find any existing nodes that it connects to in order to update, then append to list
            connected = False
            for item in connect_list:
                global nodelist
                for existing in nodelist:
                    if existing == item.node2:
                        existing.add_connection(item.distance,existing,toAdd)
                        connected = True
            if connected:
                global nodelist
                nodelist.append(toAdd)
      
    def map_network(self):
        reference_x = root.getX()
        reference_y = root.getY()
        reference_z = root.getZ()
        # assign coordinates to every connected node from the root
        # TODO


class Node(object):
    def __init__(self, space_constant1):
        global flex_constant
        flex_constant = space_constant1
        global con_front
        con_front = Connection(1,self, None)
        global con_back
        con_back = Connection(1,self, None)
        global con_left
        con_left = Connection(1,self, None)
        global con_right
        con_right = Connection(1,self, None)
        global con_top
        con_top = Connection(1,self, None)
        global con_bottom
        con_bottom = Connection(1,self, None)
    
    def set_connection(self, location, connection):
        if isinstance(connection, Connection):
            if location == 0:
                con_front = connection
            elif location == 1:
                con_back = connection
            elif location == 2:
                con_left = connection
            elif location == 3:
                con_right = connection
            elif location == 4:
                con_top = connection
            elif location == 5:
                con_bottom = connection

    def set_connections(self, connection_list):
        if isinstance(connection_list, list):
            for index, connection in enumerate(connection_list):
                if isinstance(connection, Connection):
                    if index >= 0 and index < 6:
                        Map.set_connection(index,connection)

    def get_connections(self):
        con_list = []
        if isinstance(con_front,Node):
            con_list.append(con_front)
        if isinstance(con_back,Node):
            con_list.append(con_back)
        if isinstance(con_left,Node):
            con_list.append(con_left)
        if isinstance(con_right,Node):
            con_list.append(con_right)
        if isinstance(con_top,Node):
            con_list.append(con_top)
        if isinstance(con_bottom,Node):
            con_list.append(con_bottom)
        return con_list

class LocatedNode(Node):
    # class that is fixed in space to orient other nodes.
    def __init__(self, space_constant, coord):
        upper = super(Node, self)
        upper.__init__(space_constant)
        if isinstance(coord, Coordinate):
            global coordinate
            coordinate = coord

class Connection(object):
    def __init__(self, length, Node1, Node2):
        if isinstance(Node1, Node) and isinstance(Node2, Node):
            global distance
            distance = length
            global node1
            node1 = Node1
            global node2
            node2 = Node2
    # get information
    def len(self):
        return distance
    def connect_set(self):
        return [node1, node2]
    # set information
    def set_len(self, length = 1):
        if isinstance(distance, int):
            global distance
            distance = length
    def reconnect(self,Node1, Node2):
        if isinstance(Node1, Node) and isinstance(Node2, Node):
            global node1
            node1 = Node1
            global node2
            node2 = Node2

class Coordinate(object):
    def __init__(self, x_coord, y_coord, z_coord):
        global x
        x = x_coord
        global y
        y = y_coord
        global z
        z = z_coord
    def val(self):
        return [x,y,z]