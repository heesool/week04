from version_check import is_compatible


def test_patch_update():
    assert is_compatible("1.3.7", "1.3.8")


def test_minor_update():
    assert is_compatible("1.3.7", "1.6.1")


def test_major_update():
    assert not is_compatible("1.3.7", "2.0.0")


def test_older_version():
    assert not is_compatible("1.3.7", "1.2.9")
