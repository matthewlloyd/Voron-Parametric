#!/usr/bin/python3

import drawSvg as draw


polys = [
    [(103.699, -82.118), (107.07, -82.118), (102.46, -89.131), (99.09, -89.131)],
    [(109.909, -82.118), (113.279, -82.118), (104.06, -96.142), (100.69, -96.142)],
    [(111.508, -89.131), (114.878, -89.131), (110.269, -96.142), (106.899, -96.142)]
]

min_x = min([p[0] for poly in polys for p in poly])
min_y = min([p[1] for poly in polys for p in poly])
max_x = max([p[0] for poly in polys for p in poly])
max_y = max([p[1] for poly in polys for p in poly])

print(f'min_x {min_x}')
print(f'min_y {min_y}')
print(f'max_x {max_x}')
print(f'max_y {max_y}')
print(f'width {max_x - min_x}')
print(f'height {max_y - min_y}')

scale = 1 / max( (max_y - min_y), (max_x - min_x) )
center_x = (min_x + max_x) / 2.
center_y = (min_y + max_y) / 2.

polys = [[((p[0] - center_x) * scale, (p[1] - center_y) * scale) for p in poly] for poly in polys]

for poly in polys:
    print(':'.join([f'{p[0]:.3f},{p[1]:.3f}' for p in poly]))

svg_scale = 1000
d = draw.Drawing(svg_scale, svg_scale, origin='center', displayInline=False)

for poly in polys:
    pts = []
    for p in poly:
        pts.append(p[0] * svg_scale)
        pts.append(p[1] * svg_scale)
    d.append(draw.Lines(*pts, close=True, stroke='black'))

d.saveSvg('voron_logo.svg')
