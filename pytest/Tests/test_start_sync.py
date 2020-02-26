import pytest


def test_start_sync(mainfixture):
    mainfixture.sync.just_sync()
