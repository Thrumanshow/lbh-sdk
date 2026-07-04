"""
LBH SDK v0.3.0
Suite de pruebas - test_validate.py

Valida la función validate_packet().
"""

import unittest

import lbh_sdk


VALID_FRAME = "413136005345414c00000008486f6c61204c4248"

SHORT_FRAME = "41313600"

INVALID_LENGTH = "413136005345414c00000010486f6c61204c4248"

INVALID_HEX = "413136005345414c00000008ZZZZ"


class TestValidatePacket(unittest.TestCase):

    def test_valid_packet(self):
        self.assertTrue(
            lbh_sdk.validate_packet(VALID_FRAME)
        )

    def test_short_packet(self):
        self.assertFalse(
            lbh_sdk.validate_packet(SHORT_FRAME)
        )

    def test_invalid_length(self):
        self.assertFalse(
            lbh_sdk.validate_packet(INVALID_LENGTH)
        )

    def test_invalid_hex(self):
        self.assertFalse(
            lbh_sdk.validate_packet(INVALID_HEX)
        )


if __name__ == "__main__":
    unittest.main()
