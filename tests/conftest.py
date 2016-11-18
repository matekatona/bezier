# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

"""py.test shared testing configuration.

This

* gets slow imports out of the way before running tests, so
  as not to have the cost of imports reflected in
  ``py.test --durations=N``.
"""


from matplotlib import patches
from matplotlib import path as _path_mod
import matplotlib.pyplot as plt