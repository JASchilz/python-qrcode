import unittest

from qrcode import QRCode as MacroQRCode

from uQR import QRCode as MicroQRCode


class TestMatrixCreation(unittest.TestCase):

    def test_qr_library_equivalence(self):
        """
        The `get_matrix` method of the uQR library should produce
        identical output to that of the QRCode library.
        """

        macro_qr = MacroQRCode()
        macro_qr.add_data('uQR rocks!')
        macro_matrix = macro_qr.get_matrix()

        micro_qr = MicroQRCode()
        micro_qr.add_data('uQR rocks!')
        micro_matrix = micro_qr.get_matrix()

        # The generated matrix should actually contains rows.
        self.assertGreater(len(micro_matrix), 0)

        # The uQR matrix should have the same number of rows as the
        # QRCode matrix
        self.assertEqual(len(micro_matrix), len(macro_matrix))

        for micro_row, macro_row in zip(micro_matrix, macro_matrix):
            # The row should actually contain data.
            self.assertGreater(len(micro_row), 0)

            # The two rows from the two libraries should be identical
            self.assertEqual(len(micro_row), len(macro_row))

class TestWifiCreation(unittest.TestCase):
    def test_render_matrix(self):
        micro_qr = MicroQRCode()
        ssid, password = 'test', 'test'
        micro_qr.add_data('WIFI:S:{};T:WPA;P:{};H:false;;'.format(ssid, password))
        matrix = micro_qr.render_matrix()
        self.assertGreater(len(matrix), 0)
