# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:26:49 2026

@author: Admin
"""

class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("A vector must have at least one component.")
        self.components = tuple(components)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension to be added.")
        
        added_components = (a + b for a, b in zip(self.components, other.components))
        return Vector(*added_components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __eq__(self, other):
        return isinstance(other, Vector) and self.components == other.components

v1 = Vector(2, 4)
v2 = Vector(3, 1)

v3 = v1 + v2
print(v3)  

v4 = Vector(1, 2, 3)
v5 = Vector(4, 5, 6)
print(v4 + v5)  

