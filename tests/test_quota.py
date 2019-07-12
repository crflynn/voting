"""Quota tests."""


def test_quota_method(quota_method, seats):
    assert quota_method(100, seats) > 0
