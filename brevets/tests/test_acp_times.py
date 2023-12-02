"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

from acp_times import close_time, open_time
import arrow

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_one():
    test_arrow = arrow.get('2001-01-01T01:01')
    assert close_time(200, 400, test_arrow) == arrow.get('2001-01-01T06:54')
    assert open_time(200, 400, test_arrow) == arrow.get('2001-01-01T14:21')

def test_two():
    test_arrow = arrow.get('2023-11-05T02:02')
    assert close_time(100, 600, test_arrow) == arrow.get('2023-11-05T04:58')
    assert open_time(100, 600, test_arrow) == arrow.get('2023-11-05T08:42')

def test_three():
    test_arrow = arrow.get('1900-10-03T03:03')
    assert close_time(50, 1000, test_arrow) == arrow.get('1900-10-03T04:31')
    assert open_time(50, 1000, test_arrow) == arrow.get('1900-10-03T06:33')

def test_four():
    test_arrow = arrow.get('2000-01-04T04:04')
    assert close_time(200, 200, test_arrow) == arrow.get('2000-01-04T09:57')
    assert open_time(200, 200, test_arrow) == arrow.get('2000-01-04T17:34')

def test_five():
    test_arrow = arrow.get('2024-01-05T05:05')
    assert close_time(450, 600, test_arrow) == arrow.get('2024-01-05T18:53')
    assert open_time(450, 600, test_arrow) == arrow.get('2024-01-06T11:05')
