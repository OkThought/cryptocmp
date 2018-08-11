import unittest
from datetime import datetime, timezone

import cryptocmp.historical.price.hours


class HoursTestCase(unittest.TestCase):
    def test_common(self):
        data = cryptocmp.historical.price.hours.get('BTC', 'USD', limit=1)
        for item in data:
            self.assertIn('open', item)
            self.assertIn('high', item)
            self.assertIn('low', item)
            self.assertIn('close', item)
            self.assertIn('volumefrom', item)
            self.assertIn('volumeto', item)
