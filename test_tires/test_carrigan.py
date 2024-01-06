import unittest

from carrigan_tires import CarriganTires

class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_readings = [0.9, 1, 0.8, 0.2]
        tire = CarriganTires(sensor_readings)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensor_readings = [0, 0.1, 0.8, 0.2]
        tire = CarriganTires(sensor_readings)
        self.assertFalse(tire.needs_service())