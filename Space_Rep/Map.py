import numbers

class Map(object):
    def __init__(self, space_constant = 1):
        global root
        root = FixedNode(space_constant)
        global nodelist
        nodelist = []
        nodelist.append(root)
    
    def add_node(self, toAdd):
        if isinstance(toAdd, Node):
            connect_list = toAdd.get_connections()
            # find any existing nodes that it connects to in order to update, then append to list
            for item in connect_list:
                global nodelist
                for existing in nodelist:
                    if existing == item.node2:
                        existing.add_connection(item.distance,existing,toAdd)
      
    def map_network(self):
        reference_x = root.getX()
        reference_y = root.getY()
        reference_z = root.getZ()
        # assign coordinates to every connected node from the root
        # TODO


class Node(object):
    def __init__(self, space_constant):
        global flex_constant
        flex_constant = space_constant
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
    
    def set_connection(location, connection):
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
                        set_connection(index,connection)

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

class FixedNode(Node):
    # class that is fixed in space to orient other nodes.
    def __init__(self, space_constant, x_coord = 0, y_coord = 0, z_coord = 0):
        super(Node, self).__init__(space_constant)
        if isinstance(x, numbers.Number) and isinstance(y, numbers.Number) and isinstance(z, numbers.Number):
            global x
            x = x_coord
            global y
            y = y_coord
            global z
            z = z_coord

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