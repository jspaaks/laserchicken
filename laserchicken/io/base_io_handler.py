""" Abstract IO handler """
import os

class IOHandler(object):
    """ Abstract IO handler class """
    path = None

    def __init__(self, path, mode, overwrite=False):
        """
        Perform some checks on the path where we need to operate (read/write).

        :param path: path where IO needs to take place
        :param mode: 'r' for reading, 'w' for writing
        :param overwrite: if writing, overwrite path if it already exists
        """
        self.path = path
        if mode == 'r':
            if not os.path.exists(path):
                raise OSError('{} not found.'.format(path))
        elif mode == 'w':
            if not overwrite:
                if os.path.exists(path):
                    # Raise most specific subclass of FileExistsError (3.6) and IOError (2.7).
                    raise Exception('Cannot write because path {} already exists.'.format(path))

    def read(self):
        """ Read the point cloud from disk """
        raise NotImplementedError(
            "Class %s doesn't implement read()" % (self.__class__.__name__))

    def write(self, point_cloud):
        """ Write the point cloud to disk """
        raise NotImplementedError(
            "Class %s doesn't implement write()" % (self.__class__.__name__))