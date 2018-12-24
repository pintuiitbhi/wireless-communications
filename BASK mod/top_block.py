#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Nov 19 21:18:26 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from epy_block_0 import blk
from epy_block_1 import blk
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.target_rate = target_rate = 1e6
        self.target_freq = target_freq = 433.847e6
        self.symbol_duration = symbol_duration = 0.35e-3
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_0_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)
        
        self.qtgui_sink_x_0_0.enable_rf_freq(False)
        
        
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 5000, 100, firdes.WIN_HAMMING, 6.76))
        self.epy_block_1 = blk(threshold=0.0, coeff=0.15)
        self.epy_block_0 = blk(threshold=0.5)
        self.blocks_vector_source_x_0 = blocks.vector_source_f(list(ord(i) for i in "HELLO" ), True, 1, [])
        self.blocks_throttle_2 = blocks.throttle(gr.sizeof_float*1, target_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, target_rate,True)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, int(target_rate*symbol_duration))
        self.blocks_patterned_interleaver_1 = blocks.patterned_interleaver(gr.sizeof_float*1, ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
        self.blocks_patterned_interleaver_0 = blocks.patterned_interleaver(gr.sizeof_float*1, ([1,0,2]))
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((1, ))
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/pintu/Desktop/GnuRadio/FIR Filter/output.txt", False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.analog_sig_source_x_0 = analog.sig_source_f(target_rate, analog.GR_COS_WAVE, target_freq, 1, 0)
        self.analog_const_source_x_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_patterned_interleaver_0, 1))    
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_patterned_interleaver_1, 1))    
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_patterned_interleaver_0, 2))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.blocks_patterned_interleaver_0, 0), (self.blocks_patterned_interleaver_1, 0))    
        self.connect((self.blocks_patterned_interleaver_1, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.blocks_throttle_2, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.epy_block_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.epy_block_1, 0))    
        self.connect((self.blocks_throttle_2, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_patterned_interleaver_0, 0))    
        self.connect((self.epy_block_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.epy_block_1, 0), (self.qtgui_sink_x_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_file_sink_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_target_rate(self):
        return self.target_rate

    def set_target_rate(self, target_rate):
        self.target_rate = target_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.target_rate)
        self.blocks_throttle_2.set_sample_rate(self.target_rate)
        self.blocks_throttle_0.set_sample_rate(self.target_rate)

    def get_target_freq(self):
        return self.target_freq

    def set_target_freq(self, target_freq):
        self.target_freq = target_freq
        self.analog_sig_source_x_0.set_frequency(self.target_freq)

    def get_symbol_duration(self):
        return self.symbol_duration

    def set_symbol_duration(self, symbol_duration):
        self.symbol_duration = symbol_duration

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 5000, 100, firdes.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
