#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# split chapters of source file

# chapter name : file name
intro = {
    "What is Path Integral Project?": "intro_what.rst",
    "A Brief History": "intro_history.rst",
    "Why Path Integral?": "intro_why.rst"
}

clstheo = {
    "Classical Theory: Scalar Field": "clstheo_scalar.rst",
    "Solution of Klein-Gordon Equation": "clstheo_kgeq.rst",
    "The Symmetry of Fields": "clstheo_sym_field.rst",
    "Representation of Lorentz Group": "repr_lg.rst",
    "Scalar, Spinor and Vector (Tensor) Field": "field.rst"
}

backgd = {
    "Geometric Unit System": "bg_geo_unit.rst",
    "Einstein Summation Convention": "bg_eins.rst",
    "Basic Differential Geometry": "bg_diff_geo.rst",
    "Lagrangian Dynamics of Fields": "bg_lag_dyn.rst",
    "Basic Linear Algebra": "bg_linalg.rst",
    "Basics of Lie Group Theory": "bg_liegp.rst"
}

# total data for chapter splitting
total = {}

# join chapter:file data
for chap in [intro, clstheo, backgd]:
    total.update(chap)

# preopen source file for the first close file
output = open("source.rst", 'r')

# create output file
with open("source.rst", 'r') as src:
    for line in src:
        for key, value in total.items():
            if line.startswith(key):
                output.close()
                output = open(value, 'w')
        output.write(line)
output.close()

