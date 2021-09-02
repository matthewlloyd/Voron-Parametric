#!/usr/bin/python3

import drawSvg as draw
import itertools


# scaled so overall height is 1, and logo is centered on (0, 0)
polys = [
    # outer hexagon
    ['red', (-0.433, 0.25), (0, 0.5), (0.433, 0.25), (0.433, -0.25), (0, -0.5), (-0.433, -0.25)],

    # left
    [None, (-0.312, 0), (-0.153, .276), (-0.028, 0.276), (-0.187, 0), (-0.312, 0)],
    # middle
    [None, (0.097, 0.276), (0.222, 0.276), (-0.097, -0.276), (-0.222, -0.276)],
    # right
    [None, (0.187, 0), (0.312, 0), (0.153, -0.276), (0.028, -0.276)]
]

svg_scale = 1000.
d = draw.Drawing(svg_scale, svg_scale, origin='center', displayInline=False)

for poly in polys:
    d.append(draw.Lines(
        *itertools.chain(*[(p[0] * svg_scale, p[1] * svg_scale) for p in poly[1:]]),
        close=True, stroke=poly[0], fill=poly[0]))

d.saveSvg('voron_logo.svg')
