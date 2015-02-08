import pygame_subdiv


def test_try_nodes():
    g = pygame_subdiv.Game()
    g._tree = pygame_subdiv.Tree()
    g._tree.getRoot().subDivide()
    sn0 = g._tree.getRoot().subNodes()[0]
    sn0.subDivide()
    sn1 = sn0.subNodes()[1]
    sn1.subDivide()
    sn2 = sn1.subNodes()[0]
    sn2.subDivide()
    g._tree.getRoot().subNodes()[3].subDivide()
    
    print str(g._tree)
    g._tree_to_squares()
    print repr(g._squares)
    
    
    print "Trying tree to render tree..."
    rt = g._tree_to_render_tree()
    
    def print_rt_node(node, indent_by = 1):
        indent = "   " * indent_by
        print indent + "Square " + repr(node.renderObj())
        if node.subNodes():
            for subNode in node.subNodes():
                print_rt_node(subNode, indent_by + 1)
    
    print_rt_node(rt)
