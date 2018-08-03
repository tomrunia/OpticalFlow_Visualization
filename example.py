# MIT License
#
# Copyright (c) 2018 Tom Runia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to conditions.
#
# Author: Tom Runia
# Date Created: 2018-08-03

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
import flow_vis

# Load normalized flow image of shape [H,W,2]
flow_uv = np.load('./data/flow_example_data.npy')

# Apply the coloring (for OpenCV, set convert_to_bgr=True)
flow_color = flow_vis.flow_to_color(flow_uv, convert_to_bgr=False)

# Display the image
plt.imshow(flow_color)
plt.show()











