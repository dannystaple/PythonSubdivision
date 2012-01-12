import pygame_subdiv

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