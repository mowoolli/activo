import os


def test_activo_no_args():
    cmd: int = os.system("python activo/to_shp.py")
    assert cmd == 256


def test_activo_unsupported_file():
    cmd: int = os.system("python activo/to_shp.py test.txt")
    assert cmd == 256


def test_activo_supported_file():
    cmd: int = os.system("python activo/to_shp.py test.tcx")
    assert cmd == 0