import unittest
from tire_classification import Type, classify_tire

# Call "python -m unittest" to run your test 
# Note that python might be python3 or python3.9 or whatever name you chose during installation
class TestFunction(unittest.TestCase):
    def test_invalid
        assert classify_tire(20, 30, 100) == Type.INVALID

    def test_winter
        assert classify_tire(40, 30, 120) == Type.WINTER

    def test_summer
        assert classify_tire(40, 30, 60) == Type.SUMMER

    def test_allSeason
        assert classify_tire(40, 30, 100) == Type.ALL_SEAONS
