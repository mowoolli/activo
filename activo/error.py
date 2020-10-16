__all__ = ["Error", "FileTypeError"]


class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class FileTypeError(Error):
    """Exception raised for unsupported file types.

    Attributes:
        extension (str): Unsupported file type
        message (str): Explanation of the error
    """

    def __init__(self, extension, message="Unsupported file type."):
        self.extension = extension
        self.message = message