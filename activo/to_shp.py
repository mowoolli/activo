import os
from activo import FileTypeError


def to_shp(filepath: str) -> bool:
    """
    This function accepts .tcx and .gpx files and converts them to shapefiles with linestrings.

    Args:
      filepath: The absolute path of the file to be converted

    Returns:
      True for success, False otherwise.

    """
    extension: str = str(os.path.splitext(filepath)[1])
    if extension == ".tcx":
        print("This will create a shp from a tcx.")
    elif extension == ".gpx":
        print("This will create a shp from a gpx.")
    else:
        raise FileTypeError(
            extension, extension + " file types are not supported."
        )
    return True


if __name__ == "__main__":
    import sys

    try:
        filename: str = str(sys.argv[1])
        to_shp(filename)
    except IndexError:
        print("An input file must be supplied.")
        sys.exit(1)  # abort execution
    except FileTypeError as fileErr:
        print(fileErr.message)
        sys.exit(1)  # abort execution