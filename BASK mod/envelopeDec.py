"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, threshold=0.0, coeff=0.15):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Envelope Detector',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

        self.threshold = threshold
        self.coeff = coeff

    def work(self, input_items, output_items):
        """Envelope Detect with Half/Full Wave Rectifier"""
        buf = [0] * len(input_items[0])
        a0 = self.coeff
        b1 = 1 - a0
        for i in range (0, len(input_items[0])) :
            if input_items[0][i] > self.threshold:
                buf[i] = input_items[0][i]
            else:
                buf[i] = 0
        for i in range(0, len(output_items[0])):
            if i==0:
                output_items[0][i] = a0*buf[i]
            else:
                output_items[0][i] = a0*buf[i] + b1*output_items[0][i-1]

        i = len(output_items[0])-1
        self.ry = output_items[0][i]
        return len(output_items[0])

