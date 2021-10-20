import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin_price_rate

class TestBitcoin(TestCase):
    
    @patch('bitcoin_price_rate.get_bitcoin_conversions')
    def test_calculate_bitcoin_rate(self, mock_rates):
        mock_rate = 10000.02
        mock_rate_string = "10,000.02"
        example_api_response = {"time": {"updated":"Oct 20, 2021 22:29:00 UTC","updatedISO":"2021-10-20T22:29:00+00:00","updateduk":"Oct 20, 2021 at 23:29 BST"},
        "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
        "chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate": mock_rate_string,"description":"United States Dollar","rate_float": mock_rate},
        "GBP":{"code":"GBP","symbol":"&pound;","rate": mock_rate_string,"description":"British Pound Sterling","rate_float": mock_rate},
        "EUR":{"code":"EUR","symbol":"&euro;","rate": mock_rate_string,"description":"Euro","rate_float": mock_rate}}}
        mock_rates.side_effect = [ example_api_response ]

        converted = bitcoin_price_rate.calculate_bitcoin_rate(2)
        
        expected = 20000.04

        self.assertEqual(expected, converted)

if __name__ == '__main__':
    unittest.main()