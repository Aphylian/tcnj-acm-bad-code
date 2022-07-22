from unittest import TestCase
from hamcrest import assert_that, equal_to
from src import bad


class TestBad(TestCase):
    def test_theStuff_returnsSet_ofEightElements(self):
        result = bad.the_stuff()
        expected_result = {0, -12, -1, -8, -6, -4, -3, -2}
        assert_that(result, equal_to(expected_result))

    def test_howdy_returns1_whenmIsPassedIn(self):
        result = bad.howdy('m')
        assert_that(result, equal_to(1))

    def test_howdy_returns1_whenaIsPassedIn(self):
        result = bad.howdy('a')
        assert_that(result, equal_to(19))

    def test_howdy_returns1_when10234IsPassedIn(self):
        result = bad.howdy('10234')
        assert_that(result, equal_to(10))

    def test_howdy_returns1_whensickdudesfdIsPassedIn(self):
        result = bad.howdy('sick dudesfd')
        assert_that(result, equal_to(18))

    def test_probablyOkay_returnsList_of0and1(self):
        expected_result = {0, 1}
        assert_that(bad.probably_okay(), equal_to(expected_result))

    def test_ohMy_returnsSet_of0and1and20_whenPassed1and2and0(self):
        result = bad.oh_my(1, 2, 0)
        expected_result = {0, 1, 20}
        assert_that(result, equal_to(expected_result))

    def test_ohMy_returnsSet_of16and3and7_whenPassedNegative2and2andNegative2(self):
        result = bad.oh_my(-2, 2, -2)
        expected_result = {16, 3, 7}
        assert_that(result, equal_to(expected_result))

    def test_ohMy_returnsSet_of88and105and180_whenPassed1and2and10(self):
        result = bad.oh_my(1, 2, 10)
        expected_result = {88, 105, 180}
        assert_that(result, equal_to(expected_result))

    def test_ohMy_returnsSet_of0and12and5_whenPassedNegative2and5andNegative2(self):
        result = bad.oh_my(-2, 5, -2)
        expected_result = {0, 12, 5}
        assert_that(result, equal_to(expected_result))