
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
def astar(maze, start, end):

    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create a start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(Node, end)
    end_node.g = end_node.h = end_node.f = 0

    # initialize both open and closed list
    open_list = []
    closed_list = []

    # add the start node
    open_list.append(start_node)

    # loop until you find the end
    while len(open_list) > 0:

        # get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # find the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # return the reversed path

        # generate the children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1. -1), (-1, 1), (1, -1), (1, 1)]:

            # get the node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue
                
            # create a new node
            new_node = Node(current_node, node_position)

            # append
            children.append(new_node)
        

        # loop through the children
        for child in children:

            # child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            
            # create the f, g and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            
            # add the child to the open list
            open_list.append(child)


def main():
    
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()

        

