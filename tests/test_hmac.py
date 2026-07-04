"""
LBH SDK v0.3.0
Suite de pruebas - test_hmac.py

Valida generate_hmac() y validate_hmac().
"""

import unittest

import lbh_sdk


MESSAGE = "Hola LBH"

SECRET = "HormigasAIS"

OTHER_SECRET = "OtraClave"


class TestHMAC(unittest.TestCase):

    def test_generate_hmac(self):

        digest = lbh_sdk.generate_hmac(
            MESSAGE,
            SECRET
        )

        self.assertEqual(len(digest), 64)

    def test_validate_hmac(self):

        digest = lbh_sdk.generate_hmac(
            MESSAGE,
            SECRET
        )

        self.assertTrue(
            lbh_sdk.validate_hmac(
                MESSAGE,
                SECRET,
                digest
            )
        )

    def test_invalid_secret(self):

        digest = lbh_sdk.generate_hmac(
            MESSAGE,
            SECRET
        )

        self.assertFalse(
            lbh_sdk.validate_hmac(
                MESSAGE,
                OTHER_SECRET,
                digest
            )
        )

    def test_modified_message(self):

        digest = lbh_sdk.generate_hmac(
            MESSAGE,
            SECRET
        )

        self.assertFalse(
            lbh_sdk.validate_hmac(
                MESSAGE + "!",
                SECRET,
                digest
            )
        )


if __name__ == "__main__":
    unittest.main()
