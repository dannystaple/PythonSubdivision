"""Subdiv document
Representation and behaviour of a subdiv document. Not rendering"""
import logging
import json


class SubdivDocument(object):
    
    @staticmethod
    def subdivide_node(node):
        """Subdivide a node"""
        node[:] =[[], [], [], []]

    @staticmethod
    def empty_node(node):
        """Clear the node"""
        node[:] = []
        
    @classmethod
    def make_test(cls):
        """Build a test document"""
        doc = SubdivDocument()
        cls.subdivide_node(doc._tree)
        cls.subdivide_node(doc._tree[0])
        cls.subdivide_node(doc._tree[0][1])
        cls.subdivide_node(doc._tree[0][1][0])
        return doc

    def __init__(self):
        self._tree = []
        self._filename = "test.tree"

    def get_lines(self, screen_width, screen_height):
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

        return _get_lines_for_node(self._tree, 0, 0, screen_width, screen_height)

    @staticmethod
    def load_file(self, filename):
        """Load from the filesystem"""
        doc = SubdivDocument()
        doc._file_name = filename
        with open(filename) as fp:
            doc._tree = json.load(fp)

    def save_file(self, file_name=None):
        """Save the tree to a file.
        If the kwarg is none, use an existing filename"""
        self._file_name = file_name or self._file_name
        logging.info("Writing file %s", self._file_name)
        with open(self._file_name, "w") as fp:
            json.dump(self._tree, fp)

    def get_node_at(self, x, y, screen_width, screen_height):
        """Find the node a given point, relative to the window size.
        Return parent_node, node"""
        node = self._tree
        parent_node = None
        sx, sy = 0, 0
        w, h = screen_width, screen_height
        while node != parent_node and w > 1 and h > 1 and node:
            parent_node = node
            w /= 2
            h /= 2
            if x < (sx + w):
                if y < (sy + h):
                    print "Using first sn"
                    node = parent_node[0]
                else:
                    print "Using 3rd sn"
                    sy += h
                    node = parent_node[2]
            else:
                sx += w
                if y < (sy + h):
                    print "Using 2nd sn"
                    node = parent_node[1]
                else:
                    print "Using 4th sn"
                    sy += h
                    node = parent_node[3]
        return parent_node, node
