import sys, pygame, pickle

black = 0, 0, 0
white = 0xff, 0xff, 0xff


class Node:
    def __init__(self):
        self._subNodes = None
        
    def subDivide(self):
        self._subNodes = [Node(), Node(), Node(), Node()]
    
    def subNodes(self):
        return self._subNodes
        
    def clearSubNodes(self):
        self._subNodes = None

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
        self._reset()
        self._width, self._height = 800, 800
        
    def _reset(self):
        self._lastChanged = None
        self._tree = Tree()
        self._squares = None
        
    def run(self):
        self._init_screen()
        test_tree(self._tree.getRoot())
        self._tree_to_squares()
        # self._tree_to_render_tree()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN: self.handle_click_at(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN: self.handle_key(event.key)
            self._update_display()
            
    def _init_screen(self):
        pygame.init()
        size = self._width, self._height
        self._screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Subdivision toy")

    def _tree_to_squares(self):
        """Convert a tree of nodes to squares.
        Each node will result in 4 subdivisions."""
        def _get_squares_for_node(node, x, y, width, height):
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
        for square in self._squares:
            pygame.draw.rect(self._screen, black, square, 2)
        pygame.display.flip()
    
    def handle_key(self, key):
        """Handle keypresses"""
        key = key & 0xff
        print "Handling key '" + chr(key) + "'" 
        if chr(key) == 'q':
            sys.exit()
        if chr(key) == 'c':
            self._reset()
            self._tree_to_squares()
        if chr(key) == 's':
            with open("test.tree","w") as fp:
                pickle.dump(self._tree, fp)
        if chr(key) == 'l':
            self._lastChanged = None
            with open("test.tree") as fp:
                self._tree = pickle.load(fp)
            self._tree_to_squares()
        if chr(key) == 'u' and self._lastChanged:
            self._lastChanged.clearSubNodes()
            self._tree_to_squares()
            self._lastChanged = None
        
    def handle_click_at(self, pos):
        """Given a click at an x,y tuple (pos) it should subdivide the node it landed on"""
        x,y = pos
        node = None
        newNode = self._tree.getRoot()
        sx = 0
        sy = 0
        w = self._width
        h = self._height
        while newNode != node and w > 1 and h > 1 and newNode.subNodes():
            node = newNode
            w /= 2
            h /= 2
            if x < (sx + w):
                if y < (sy + h):
                    print "Using first sn"
                    newNode = node.subNodes()[0]
                else:
                    print "Using 3rd sn"
                    sy += h
                    newNode = node.subNodes()[2]
            else:
                sx += w
                if y < (sy + h):
                    print "Using 2nd sn"
                    newNode = node.subNodes()[1]
                else:
                    print "Using 4th sn"
                    sy += h
                    newNode = node.subNodes()[3]
        newNode.subDivide()
        self._lastChanged = newNode
        self._tree_to_squares()
    
    # def mouse_func(self):
    #     use boundaries to find square that got clicked
    #     subdivide the square (update tree and squares tree)
        
if __name__ == '__main__':
    Game().run()