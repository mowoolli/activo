def test_tcx_to_shp():
    from activo import to_shp

    assert to_shp("test.tcx") == True


def test_gpx_to_shp():
    from activo import to_shp

    assert to_shp("test.gpx") == True


def test_unsupported_to_shp():
    import pytest
    from activo import FileTypeError
    from activo import to_shp

    with pytest.raises(FileTypeError):
        to_shp("test.txt")
