"""
LBH SDK v0.3.0
Suite de pruebas - test_encode.py

Valida la función encode_packet()
"""

import unittest

import lbh_sdk


class TestEncodePacket(unittest.TestCase):

    def test_encode_packet(self):

        frame = lbh_sdk.encode_packet(
            "41313600",
            "5345414c",
            "Hola LBH"
        )

        self.assertEqual(
            frame,
            "413136005345414c00000008486f6c61204c4248"
        )

    def test_header(self):

        frame = lbh_sdk.encode_packet(
            "41313600",
            "5345414c",
            "Hola LBH"
        )

        self.assertEqual(frame[:8], "41313600")

    def test_type_code(self):

        frame = lbh_sdk.encode_packet(
            "41313600",
            "5345414c",
            "Hola LBH"
        )

        self.assertEqual(frame[8:16], "5345414c")

    def test_length(self):

        frame = lbh_sdk.encode_packet(
            "41313600",
            "5345414c",
            "Hola LBH"
        )

        self.assertEqual(frame[16:24], "00000008")


if __name__ == "__main__":
    unittest.main()
