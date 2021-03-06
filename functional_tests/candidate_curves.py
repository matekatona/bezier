# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

import bezier

import runtime_utils


CURVES = (
    None,  # Start counting at one.
    # g1 = sympy.Matrix([[s, 2 * s * (1 - s)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.0],
        [0.5, 1.0],
        [1.0, 0.0],
    ]), _copy=False),
    # g2 = sympy.Matrix([[(9 - 8 * s) / 8, (2 * s - 1)**2 / 2]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [1.125, 0.5],
        [0.625, -0.5],
        [0.125, 0.5],
    ]), _copy=False),
    # g3 = 3 * g1
    # g3 = sympy.Matrix([[3 * s, 6 * s * (1 - s)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.0],
        [1.5, 3.0],
        [3.0, 0.0],
    ]), _copy=False),
    # g4 = sympy.Matrix([[
    #     -3 * (4 * s**2 + s - 4) / 4,
    #     (92 * s**2 - 77 * s + 24) / 16,
    # ]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [3.0, 1.5],
        [2.625, -0.90625],
        [-0.75, 2.4375],
    ]), _copy=False),
    # g5 = sympy.Matrix([[s, (8 * s**2 - 8 * s + 3) / 4]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.75],
        [0.5, -0.25],
        [1.0, 0.75],
    ]), _copy=False),
    # g6 = sympy.Matrix([[s, s**2 + (1 - s)**2]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 1.0],
        [0.5, 0.0],
        [1.0, 1.0],
    ]), _copy=False),
    # g7 = sympy.Matrix([[s, (4 * s**2 - 4 * s + 17) / 64]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.265625],
        [0.5, 0.234375],
        [1.0, 0.265625],
    ]), _copy=False),
    # g8 = sympy.Matrix([[8 * s, 3]]) / 8
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.375],
        [1.0, 0.375],
    ]), _copy=False),
    # g9 = sympy.Matrix([[2, 3 * s]]) / 4
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.5, 0.0],
        [0.5, 0.75],
    ]), _copy=False),
    # g10 = 9 * g1
    # g10 = sympy.Matrix([[9 * s, 18 * s * (1 - s)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.0],
        [4.5, 9.0],
        [9.0, 0.0],
    ]), _copy=False),
    # g11 = sympy.Matrix([[6 * s, 8 * (1 - s)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 8.0],
        [6.0, 0.0],
    ]), _copy=False),
    # NOTE: This curve has a self-crossing.
    # g12 = sympy.Matrix([[
    #     -3 * s * (3 * s - 2)**2 / 4,
    #     -(27 * s**3 - 72 * s**2 + 48 * s - 16) / 8,
    # ]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 2.0],
        [-1.0, 0.0],
        [1.0, 1.0],
        [-0.75, 1.625],
    ]), _copy=False),
    # g13 = sympy.Matrix([[s, 4 * s * (1 - s) * (7 * s**2 - 7 * s + 2)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.0],
        [0.25, 2.0],
        [0.5, -2.0],
        [0.75, 2.0],
        [1.0, 0.0],
    ]), _copy=False),
    # g14 = sympy.Matrix([[3 * s / 4, 3 * s * (4 - 3 * s) / 8]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.0],
        [0.375, 0.75],
        [0.75, 0.375],
    ]), _copy=False),
    # g15 = sympy.Matrix([[(3 * s + 1) / 4, (9 * s**2 - 6 * s + 5) / 8]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.25, 0.625],
        [0.625, 0.25],
        [1.0, 1.0],
    ]), _copy=False),
    # g16 = sympy.Matrix([[(3 * s + 1) / 4, 3 * (6 * s**2 - 4 * s + 3) / 16]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.25, 0.5625],
        [0.625, 0.1875],
        [1.0, 0.9375],
    ]), _copy=False),
    # g17 = sympy.Matrix([[11 - 8 * s, -4 * (2 * s**2 - s - 2)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [11.0, 8.0],
        [7.0, 10.0],
        [3.0, 4.0],
    ]), _copy=False),
    # g18 = sympy.Matrix([[s + 1, -2 * s * (1 - s)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [1.0, 0.0],
        [1.5, -1.0],
        [2.0, 0.0],
    ]), _copy=False),
    # g19 = sympy.Matrix([[s + 1, 2 * s * (1 - s)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [2.0, 0.0],
        [1.5, 1.0],
        [1.0, 0.0],
    ]), _copy=False),
    # g20 = sympy.Matrix([[(2 * s - 1)**2, s/2]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [1.0, 0.0],
        [-1.0, 0.25],
        [1.0, 0.5],
    ]), _copy=False),
    # g21 = sympy.Matrix([[
    #     (10 * s - 1) / 8,
    #     (9 - 10 * s) * (10 * s - 1) / 32,
    # ]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [-0.125, -0.28125],
        [0.5, 1.28125],
        [1.125, -0.28125],
    ]), _copy=False),
    # g22 = sympy.Matrix([[25 * (2 * s - 1)**2 / 16, (10 * s - 1)  / 16]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [1.5625, -0.0625],
        [-1.5625, 0.25],
        [1.5625, 0.5625],
    ]), _copy=False),
    # g23 = 5 * g8 + sympy.Matrix([[24, 21]]) / 8
    # g23 = sympy.Matrix([[10 * s + 6, 9]]) / 2
    bezier.Curve.from_nodes(np.asfortranarray([
        [3.0, 4.5],
        [8.0, 4.5],
    ]), _copy=False),
    # NOTE: This is coincident with CURVE1.
    #       g1([1/4, 1]) == g24([0, 3/4])
    # g24 = sympy.Matrix([[(4 * s + 1) / 4, (3 - 4 * s) * (4 * s + 1) / 8]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.25, 0.375],
        [0.75, 0.875],
        [1.25, -0.625],
    ]), _copy=False),
    # g25 = sympy.Matrix([[
    #     -s * (2 * s**2 - 3 * s - 3) / 4,
    #     -(3 * s**3 - 3 * s - 1) / 2,
    # ]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.5],
        [0.25, 1.0],
        [0.75, 1.5],
        [1.0, 0.5],
    ]), _copy=False),
    # g26 = sympy.Matrix([[
    #     3 * (14 * s + 1) / 8,
    #     18 * s**3 - 27 * s**2 + 3 * s + 7,
    # ]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.375, 7.0],
        [2.125, 8.0],
        [3.875, 0.0],
        [5.625, 1.0],
    ]), _copy=False),
    # g27 = sympy.Matrix([[
    #     (6 * s + 1) / 8,
    #     (35 * s**3 - 60 * s**2 + 24 * s + 4) / 16,
    # ]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.125, 0.25],
        [0.375, 0.75],
        [0.625, 0.0],
        [0.875, 0.1875],
    ]), _copy=False),
    # NOTE: Though curves 1 and 6 successfully intersect (at a point
    #       of tangency), the rotated equivalents do not.
    # Rotate g1 by 45 degrees and scale by sqrt(2).
    # g28 = sympy.Matrix([[s * (2 * s - 1), s * (3 - 2 * s)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 0.0],
        [-0.5, 1.5],
        [1.0, 1.0],
    ]), _copy=False),
    # Rotate g6 by 45 degrees and scale by sqrt(2).
    # g29 = sympy.Matrix([[(1 - 2 * s) * (1 - s), 2 * s**2 - s + 1]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [-1.0, 1.0],
        [0.5, 0.5],
        [0.0, 2.0],
    ]), _copy=False),
    # Rotate g9 by 45 degrees and scale by sqrt(2).
    # g30 = sympy.Matrix([[(2 - 3 * s) / 4, (2 + 3 * s) / 4]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.5, 0.5],
        [-0.25, 1.25],
    ]), _copy=False),
    # g31 = 2 * g11 + sympy.Matrix([[1, 3]]) / 4
    # g31 = sympy.Matrix([[(48 * s + 1) / 4, (67 - 64 * s) / 4]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.25, 16.75],
        [12.25, 0.75],
    ]), _copy=False),
    # g32 = sympy.Matrix([[(7 * s - 2) / 8, -1 / 4]])
    # NOTE: This is a degree-elevated line.
    bezier.Curve.from_nodes(np.asfortranarray([
        [-0.25, -0.25],
        [0.1875, -0.25],
        [0.625, -0.25],
    ]), _copy=False),
    # g33 = sympy.Matrix([[(1 - 2 * s) * (s - 1) / 8, -s]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [-0.125, 0.0],
        [0.0625, -0.5],
        [0.0, -1.0],
    ]), _copy=False),
    # g34 = sympy.Matrix([[4, 3 * (2 * s + 5)]]) / 8
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.5, 1.875],
        [0.5, 2.625],
    ]), _copy=False),
    # g35 = sympy.Matrix([[5 * (1 - 2 * s), 21]]) / 8
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.625, 2.625],
        [-0.625, 2.625],
    ]), _copy=False),
    # g36 = sympy.Matrix([[(1 - s) / 2, -3 * (s + 1) / 8]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.5, -0.375],
        [0.0, -0.75],
    ]), _copy=False),
    # g37 = sympy.Matrix([[(7 * s - 2) / 4, 7 * (s - 1) / 8]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [-0.5, -0.875],
        [1.25, 0.0],
    ]), _copy=False),
    # g38 = sympy.Matrix([[(3 * s + 1) / 2, (3 * s - 1)**2 / 8]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.5, 0.125],
        [1.25, -0.25],
        [2.0, 0.5],
    ]), _copy=False),
    # g39 = sympy.Matrix([[(2 * s + 1) / 2, -(2 * s - 1)**2 / 8]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.5, -0.125],
        [1.0, 0.125],
        [1.5, -0.125],
    ]), _copy=False),
    # g40 is not worth writing down
    bezier.Curve.from_nodes(np.asfortranarray([
        [float.fromhex('-0x1.1f2347525aff1p-2'),
         float.fromhex('-0x1.b10f43da717d8p-3')],
        [float.fromhex('-0x1.3912a66009422p-2'),
         float.fromhex('-0x1.263d62f131d03p-4')],
    ]), _copy=False),
    # g41 is not worth writing down
    bezier.Curve.from_nodes(np.asfortranarray([
        [float.fromhex('-0x1.25a8a28e98475p-2'),
         float.fromhex('-0x1.692bd46818fe8p-3')],
        [float.fromhex('-0x1.7daf3df0a049ep-2'),
         float.fromhex('-0x1.1361ffff031f1p-2')],
    ]), _copy=False),
    # g42 = g12([0, 0.5])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 2.0],
        [-0.5, 1.0],
        [-0.25, 0.75],
        [-0.09375, 0.828125],
    ]), _copy=False),
    # g43 = g12([0.5, 1])
    bezier.Curve.from_nodes(np.asfortranarray([
        [-0.09375, 0.828125],
        [0.0625, 0.90625],
        [0.125, 1.3125],
        [-0.75, 1.625],
    ]), _copy=False),
    # g44 = g12([0, 0.25])
    bezier.Curve.from_nodes(np.asfortranarray([
        [0.0, 2.0],
        [-0.25, 1.5],
        [-0.3125, 1.1875],
        [-75.0 / 256.0, 517.0 / 512.0],
    ]), _copy=False),
    # g45 = g12([0.25, 0.5])
    bezier.Curve.from_nodes(np.asfortranarray([
        [-75.0 / 256.0, 517.0 / 512.0],
        [-35.0 / 128.0, 213.0 / 256.0],
        [-0.171875, 101.0 / 128.0],
        [-0.09375, 0.828125],
    ]), _copy=False),
    # g46 = g12([0.5, 0.75])
    bezier.Curve.from_nodes(np.asfortranarray([
        [-0.09375, 0.828125],
        [-1.0 / 64.0, 111.0 / 128.0],
        [5.0 / 128.0, 253.0 / 256.0],
        [-9.0 / 256.0, 583.0 / 512.0],
    ]), _copy=False),
    # g47 = g12([0.75, 1])
    bezier.Curve.from_nodes(np.asfortranarray([
        [-9.0 / 256.0, 583.0 / 512.0],
        [-0.109375, 1.2890625],
        [-0.3125, 1.46875],
        [-0.75, 1.625],
    ]), _copy=False),
    # g48 = sympy.Matrix([[1, 3 * (2 * s - 1)]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [1.0, -3.0],
        [1.0, 3.0],
    ]), _copy=False),
    # g49 = sympy.Matrix([[10 * (1 - s), 0]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [10.0, 0.0],
        [0.0, 0.0],
    ]), _copy=False),
    # g50 = sympy.Matrix([[(18 - s) / 8, (97 - 5 * s) / 32]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [2.25, 3.03125],
        [2.125, 2.875],
    ]), _copy=False),
    # g51 = sympy.Matrix([[(3 * s + 34) / 16, (92 - s) / 32]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [2.125, 2.875],
        [2.3125, 2.84375],
    ]), _copy=False),
    # NOTE: This is g50, but degree elevated.
    # g52 = sympy.Matrix([[(18 - s) / 8, (97 - 5 * s) / 32]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [2.25, 3.03125],
        [2.1875, 2.953125],
        [2.125, 2.875],
    ]), _copy=False),
    # NOTE: This is g51, but degree elevated.
    # g53 = sympy.Matrix([[(3 * s + 34) / 16, (92 - s) / 32]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [2.125, 2.875],
        [2.21875, 2.859375],
        [2.3125, 2.84375],
    ]), _copy=False),
    # NOTE: This curve has a "bad" parameterization. It is a line, but
    #       the curve appears quadratic. There are no self-intersections
    #       or cusps in [0, 1], but the curve should be degree 1.
    # g54 = sympy.Matrix([[(s**2 + 60 * s + 1076) / 512, 23 / 8]])
    bezier.Curve.from_nodes(np.asfortranarray([
        [2.1015625, 2.875],
        [2.16015625, 2.875],
        [2.220703125, 2.875],
    ]), _copy=False),
)

_SQ31 = np.sqrt(31.0)
_D33 = 2.0 / np.sqrt(33.0)
_SQ7 = np.sqrt(7.0)
_D7 = 0.5 / _SQ7
_D5 = np.sqrt(5.0) / 8.0
_SQ5 = np.sqrt(5.0)
_S_ROOT1, _S_ROOT2, _ = runtime_utils.real_roots(
    [17920, -29760, 13512, -1691])
_T_ROOT1, _T_ROOT2, _ = runtime_utils.real_roots([35, -60, 24, -2])
# Accurate version of 4 sqrt(57) - 30
_S_ROOT3 = float.fromhex('0x1.983e62b67adeep-3')
_EMPTY = np.zeros((0, 4), order='F')
# NOTE: The intersection information is in 4 columns. The first
#       column is the s-parameter, the second is the t-parameter, and
#       third is the x-value at the intersection and finally the y-value.
INTERSECTION_INFO = {
    (1, 2): np.asfortranarray([
        [0.0625 * (9.0 - _SQ31), 0.0625 * (9.0 + _SQ31),
         0.0625 * (9.0 - _SQ31), (16.0 + _SQ31) / 64.0],
        [0.0625 * (9.0 + _SQ31), 0.0625 * (9.0 - _SQ31),
         0.0625 * (9.0 + _SQ31), (16.0 - _SQ31) / 64.0],
    ]),
    (3, 4): np.asfortranarray([
        [0.25, 0.75, 0.75, 1.125],
        [0.875, 0.25, 2.625, 0.65625],
    ]),
    (1, 5): np.asfortranarray([
        [0.25, 0.25, 0.25, 0.375],
        [0.75, 0.75, 0.75, 0.375],
    ]),
    (1, 6): np.asfortranarray([
        [0.5, 0.5, 0.5, 0.5],
    ]),
    (1, 7): np.asfortranarray([
        [0.5 - _D33, 0.5 - _D33, 0.5 - _D33, 17.0 / 66.0],
        [0.5 + _D33, 0.5 + _D33, 0.5 + _D33, 17.0 / 66.0],
    ]),
    (1, 8): np.asfortranarray([
        [0.25, 0.25, 0.25, 0.375],
        [0.75, 0.75, 0.75, 0.375],
    ]),
    (1, 9): np.asfortranarray([
        [0.5, 2.0 / 3.0, 0.5, 0.5],
    ]),
    (10, 11): np.asfortranarray([
        [1.0 / 3.0, 0.5, 3.0, 4.0],
    ]),
    (8, 9): np.asfortranarray([
        [0.5, 0.5, 0.5, 0.375],
    ]),
    (1, 13): np.asfortranarray([
        [0.0, 0.0, 0.0, 0.0],
        [0.5 - _D7, 0.5 - _D7, 0.5 - _D7, 3.0 / 7.0],
        [0.5 + _D7, 0.5 + _D7, 0.5 + _D7, 3.0 / 7.0],
        [1.0, 1.0, 1.0, 0.0],
    ]),
    (14, 15): np.asfortranarray([
        [2.0 / 3.0, 1.0 / 3.0, 0.5, 0.5],
    ]),
    (14, 16): np.asfortranarray([
        [0.5, 1.0 / 6.0, 0.375, 0.46875],
        [5.0 / 6.0, 0.5, 0.625, 0.46875],
    ]),
    (10, 17): np.asfortranarray([
        [1.0 / 3.0, 1.0, 3.0, 4.0],
    ]),
    (1, 18): np.asfortranarray([
        [1.0, 0.0, 1.0, 0.0],
    ]),
    (1, 19): np.asfortranarray([
        [1.0, 1.0, 1.0, 0.0],
    ]),
    (1, 20): np.asfortranarray([
        [0.375 - _D5, 0.625 - _D5, 0.375 - _D5, 0.3125 - 0.5 * _D5],
        [0.25, 0.75, 0.25, 0.375],
        [0.375 + _D5, 0.625 + _D5, 0.375 + _D5, 0.3125 + 0.5 * _D5],
        [1.0, 0.0, 1.0, 0.0],
    ]),
    (20, 21): np.asfortranarray([
        [0.0, 9.0 / 10.0, 1.0, 0.0],
        [0.625 - 0.125 * _SQ5, (4.0 - _SQ5) / 10.0,
         0.375 - 0.125 * _SQ5, 0.3125 - 0.0625 * _SQ5],
        [0.75, 3.0 / 10.0, 0.25, 0.375],
        [0.625 + 0.125 * _SQ5, (4.0 + _SQ5) / 10.0,
         0.375 + 0.125 * _SQ5, 0.3125 + 0.0625 * _SQ5],
    ]),
    (21, 22): np.asfortranarray([
        [(4.0 - _SQ5) / 10.0, (6.0 - _SQ5) / 10.0,
         0.375 - 0.125 * _SQ5, 0.3125 - 0.0625 * _SQ5],
        [3.0 / 10.0, 7.0 / 10.0, 0.25, 0.375],
        [(4.0 + _SQ5) / 10.0, (6.0 + _SQ5) / 10.0,
         0.375 + 0.125 * _SQ5, 0.3125 + 0.0625 * _SQ5],
        [9.0 / 10.0, 1.0 / 10.0, 1.0, 0.0],
    ]),
    (10, 23): np.asfortranarray([
        [0.5, 3.0 / 10.0, 4.5, 4.5],
    ]),
    # NOTE: This is coincident curves.
    (1, 24): np.asfortranarray([
        [0.25, 0.0, 0.25, 0.375],
        [1.0, 0.75, 1.0, 0.0],
    ]),
    (15, 25): np.asfortranarray([
        # ctx = mpmath.MPContext()
        # ctx.prec = 200
        # s --> ctx.polyroots([486, -3726, 13905, -18405, 6213, 1231])
        # t --> ctx.polyroots([4, -16, 13, 25, -28, 4])
        # x --> (3 s + 1) / 4
        # y --> (9 s^2 - 6 s + 5) / 8
        [float.fromhex('0x1.b7b348cf939b9p-1'),
         float.fromhex('0x1.bf3536665a0cdp-1'),
         float.fromhex('0x1.c9c6769baeb4ap-1'),
         float.fromhex('0x1.9f09401c281ddp-1')]
    ]),
    (11, 26): np.asfortranarray([
        [0.5 - 7.0 * _SQ7 / 48.0, 0.5 - _SQ7 / 6.0,
         3.0 - 0.875 * _SQ7, 4.0 + 7.0 * _SQ7 / 6.0],
        [0.5, 0.5, 3.0, 4.0],
        [0.5 + 7.0 * _SQ7 / 48.0, 0.5 + _SQ7 / 6.0,
         3.0 + 0.875 * _SQ7, 4.0 - 7.0 * _SQ7 / 6.0],
    ]),
    (8, 27): np.asfortranarray([
        [_S_ROOT1, _T_ROOT1, _S_ROOT1, 0.375],
        [_S_ROOT2, _T_ROOT2, _S_ROOT2, 0.375],
    ]),
    (28, 29): np.asfortranarray([
        [0.5, 0.5, 0.0, 1.0],
    ]),
    (29, 30): np.asfortranarray([
        [0.5, 2.0 / 3.0, 0.0, 1.0],
    ]),
    (8, 23): _EMPTY,
    (11, 31): _EMPTY,
    (32, 33): np.asfortranarray([
        [13.0 / 56.0, 0.25, -0.046875, -0.25],
    ]),
    (34, 35): np.asfortranarray([
        [1.0, 1.0 / 10.0, 0.5, 2.625],
    ]),
    (36, 37): np.asfortranarray([
        [0.0, 4.0 / 7.0, 0.5, -0.375],
    ]),
    (38, 39): np.asfortranarray([
        [1.0 / 3.0, 0.5, 1.0, 0.0],
    ]),
    (40, 41): _EMPTY,
    (42, 43): np.asfortranarray([
        [1.0 - _SQ5 / 3.0, _SQ5 / 3.0, -0.25, 1.375],
        [1.0, 0.0, -0.09375, 0.828125],
    ]),
    (44, 45): np.asfortranarray([
        [1.0, 0.0, -75.0 / 256.0, 517.0 / 512.0],
    ]),
    (46, 47): np.asfortranarray([
        [1.0, 0.0, -9.0 / 256.0, 583.0 / 512.0],
    ]),
    (48, 49): np.asfortranarray([
        [0.5, 9.0 / 10.0, 1.0, 0.0],
    ]),
    (50, 54): np.asfortranarray([
        [1.0, _S_ROOT3, 2.125, 2.875],
    ]),
    (51, 54): np.asfortranarray([
        [0.0, _S_ROOT3, 2.125, 2.875],
    ]),
    (52, 54): np.asfortranarray([
        [1.0, _S_ROOT3, 2.125, 2.875],
    ]),
    (53, 54): np.asfortranarray([
        [0.0, _S_ROOT3, 2.125, 2.875],
    ]),
}
