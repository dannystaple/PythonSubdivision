import json
import sys, pygame
import time

black = 0, 0, 0
white = 0xff, 0xff, 0xff


def subdivide():
    return [[], [], [], []]


def test_tree():
    tree = subdivide()
    tree[0] = subdivide()
    tree[0][1] = subdivide()
    tree[0][1][0] = subdivide()
    return tree


class Game:
    _tree = []
    _lastChanged = None
    _lines = None
    _file_name = None
    _screen = None

    def __init__(self):
        self._reset()
        self._width, self._height = 640, 640
        self._tree = test_tree()
        self._file_name = "test.tree"

    def _reset(self):
        self._lastChanged = None
        self._tree = []
        self._lines = None

    def run(self):
        self._init_screen()
        self._tree_to_lines()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click_at(pygame.mouse.get_pos(), event.button)
                if event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)
            self._update_display()
            time.sleep(0.1)

    def _init_screen(self):
        pygame.init()
        size = self._width, self._height
        self._screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Subdivision toy")

    def _tree_to_lines(self):
        """Convert a tree of nodes to lines.
        Each node will result in 4 subdivisions."""

        def _get_lines_for_node(sub_nodes, x, y, width, height):
            hwidth = width / 2
            hheight = height / 2
            if hwidth >= 1 and hheight >= 1 and sub_nodes:
                return (_get_lines_for_node(sub_nodes[0], x, y, hwidth, hheight) +
                        _get_lines_for_node(sub_nodes[1], x + hwidth, y, hwidth, hheight) +
                        _get_lines_for_node(sub_nodes[2], x, y + hheight, hwidth, hheight) +
                        _get_lines_for_node(sub_nodes[3], x + hwidth, y + hheight, hwidth, hheight))
            else:
                return [[x, y, x+width, y], [x, y, x, y+height]]

        self._lines = _get_lines_for_node(self._tree, 0, 0, self._width, self._height)

    def _update_display(self):
        self._screen.fill(white)
        # render lines from tree
        for line in self._lines:
            pygame.draw.line(self._screen, black, line[:2], line[2:], 1)
        pygame.display.flip()

    def load_file(self, filename):
        self._lastChanged = None
        self._file_name = filename
        with open(filename) as fp:
            self._tree = json.load(fp)
        print("Loaded file %s" % self._file_name)
        self._tree_to_lines()
        print("Converted to tree")

    def save_file(self):
        print("Writing file %s" % self._file_name)
        with open(self._file_name, "w") as fp:
            json.dump(self._tree, fp)

    def handle_key(self, key):
        """Handle keypresses"""
        key &= 0xff
        print("Handling key '" + chr(key) + "'")
        if chr(key) == 'q':
            sys.exit()
        if chr(key) == 'c':
            self._reset()
            self._tree_to_lines()
        if chr(key) == 's':
            self.save_file()
        if chr(key) == 'l':
            self.load_file(self._file_name)
        if chr(key) == 'u' and self._lastChanged:
            self._lastChanged.clearSubNodes()
            self._tree_to_lines()
            self._lastChanged = None

    def handle_click_at(self, pos, button):
        """Given a click at an x,y tuple (pos) it should subdivide the node it landed on"""
        x, y = pos
        node = None
        new_node = self._tree
        sx = 0
        sy = 0
        w = self._width
        h = self._height
        while new_node != node and w > 1 and h > 1 and new_node:
            node = new_node
            w /= 2
            h /= 2
            if x < (sx + w):
                if y < (sy + h):
                    print("Using first sn")
                    new_node = node[0]
                else:
                    print("Using 3rd sn")
                    sy += h
                    new_node = node[2]
            else:
                sx += w
                if y < (sy + h):
                    print("Using 2nd sn")
                    new_node = node[1]
                else:
                    print("Using 4th sn")
                    sy += h
                    new_node = node[3]
        if button == 1:
            new_node.extend(subdivide())
            self._lastChanged = new_node
            self._tree_to_lines()
        if button == 3 and node != self._tree:
            node[:] = []
            self._tree_to_lines()


if __name__ == '__main__':
    g = Game()
    if len(sys.argv) > 1:
        g.load_file(sys.argv[1])
    g.run()
