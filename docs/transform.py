#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# read in source.md and remove script for mathjax

# open and manipulate file
with open("raw_source.md", 'r') as mdsrc:
    with open("source.md", 'wb') as output:
        for line in mdsrc:
            # transform aligned to $$
            if line.startswith(r'\begin{aligned') \
                or line.startswith(r'\end{aligned'):
                output.write("$$\n")
                continue
            if line.startswith(r'> \begin{aligned') \
                or line.startswith(r'> \end{aligned'):
                output.write("$$\n")
                continue
            # transform !! to .. note::
            if line.startswith(r"!!"):
                output.write(line.replace("!!", ".. note::"))
                continue
            # transform ! to .. warning::
            if line.startswith(r"!"):
                output.write(line.replace("!", ".. warning::"))
                continue
            # delete scripts for mathjax in markdown
            if not line.startswith('<script type="text/x-mathjax-config">') \
                and not line.startswith('<script type="text/javascript"'):
                output.write(line)

