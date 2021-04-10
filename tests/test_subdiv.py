import pygame_subdiv


def test_make_tree():
    tree = pygame_subdiv.subdivide()
    assert tree == [[], [], [], []]



