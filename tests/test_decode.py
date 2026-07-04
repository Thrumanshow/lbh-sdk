"""
LBH SDK v0.3.0
Suite de pruebas - test_decode.py

Valida la función decode_packet()
"""

import unittest

import lbh_sdk


FRAME = "413136005345414c00000008486f6c61204c4248"


class TestDecodePacket(unittest.TestCase):

    def test_decode_packet(self):

        packet = lbh_sdk.decode_packet(FRAME)

        self.assertEqual(packet["header"], "41313600")
        self.assertEqual(packet["type_code"], "5345414c")
        self.assertEqual(packet["length"], 8)
        self.assertEqual(packet["payload"], "Hola LBH")

    def test_header(self):

        packet = lbh_sdk.decode_packet(FRAME)

        self.assertEqual(packet["header"], "41313600")

    def test_type_code(self):

        packet = lbh_sdk.decode_packet(FRAME)

        self.assertEqual(packet["type_code"], "5345414c")

    def test_payload(self):

        packet = lbh_sdk.decode_packet(FRAME)

        self.assertEqual(packet["payload"], "Hola LBH")


if __name__ == "__main__":
    unittest.main()
