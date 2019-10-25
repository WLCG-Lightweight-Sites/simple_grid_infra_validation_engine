class ComponentNotInstalledError(Exception):
    """ Raised when a framework component is not installed"""
    pass

class DirectoryNotFoundError(Exception):
    """Raised when a directory is excpected but not found"""
    pass

class PackageNotInstalledError(Exception):
    """Raised when a package is expected but not installed"""
    pass
