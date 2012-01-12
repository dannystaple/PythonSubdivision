import sys, pygame

black = 0, 0, 0
white = 0xff, 0xff, 0xff

class Node:
    def __init__(self):
        self._subNodes = None
        
    def subDivide(self):
        self._subNodes = [Node(), Node(), Node(), Node()]
    
    def subNodes(self):
        return self._subNodes
        
class Tree:
    def __init__(self):
        self._root = Node()
        
    def getRoot(self):
        """Get the tree root"""
        return self._root

def test_tree(root):
    root.subDivide()
    sn0 = root.subNodes()[0]
    sn0.subDivide()
    sn1 = sn0.subNodes()[1]
    sn1.subDivide()
    sn2 = sn1.subNodes()[0]
    sn2.subDivide()
    
class Game:
    def __init__(self):
        self._tree = None
        self._squares = None
        self._width, self._height = 800, 800
        
    def run(self):
        self._tree = Tree()
        self._init_screen()
        test_tree(self._tree.getRoot())
        self._tree_to_squares()
        
        self._update_display()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
    def _init_screen(self):
        pygame.init()
        size = self._width, self._height
        self._screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Subdivision toy")

    def _tree_to_squares(self):
        """Convert a tree of nodes to squares.
        Each node will result in 4 subdivisions."""
        def _get_squares_for_node(node, x, y, width, height):
            squares = [[x, y, width,height]]
            hwidth = width / 2
            hheight = height / 2
            subNodes = node.subNodes()
            if hwidth >=1 and hheight >= 1 and subNodes:
                return (_get_squares_for_node(subNodes[0], x, y, hwidth, hheight) + 
                    _get_squares_for_node(subNodes[1], x + hwidth, y, hwidth, hheight) + 
                    _get_squares_for_node(subNodes[2], x, y + hheight, hwidth, hheight) +
                    _get_squares_for_node(subNodes[3], x + hwidth, y + hheight, hwidth, hheight))
            else:
                return [[x, y, width,height]]
        self._squares = _get_squares_for_node(self._tree.getRoot(), 0, 0, self._width, self._height)
        
    def _update_display(self):        
        self._screen.fill(white)
        # render squares from tree
        # pygame.draw.rect(self._screen, (0xff, 0x00, 0x00), (10, 10, 50, 50), 5)
        for square in self._squares:
            print "drawing " + repr(square)
            pygame.draw.rect(self._screen, black, square, 2)
        pygame.display.flip()
    # 
    # def mouse_func(self):
    #     use boundaries to find square that got clicked
    #     subdivide the square (update tree and squares tree)
        
if __name__ == '__main__':
    Game().run()