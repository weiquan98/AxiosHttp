# test_axioshttp.py
"""
Tests for AxiosHttp module.
"""

import unittest
from axioshttp import AxiosHttp

class TestAxiosHttp(unittest.TestCase):
    """Test cases for AxiosHttp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AxiosHttp()
        self.assertIsInstance(instance, AxiosHttp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AxiosHttp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
