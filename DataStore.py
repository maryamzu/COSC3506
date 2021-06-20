import jsonpickle
from threading import Thread, Event


class DataStore:
    """ The data store class provides methods for loading, storing, saving and autosaving data to a file.
    The data field can be any object serializable by jsonpickle."""

    def __init__(self, file_name):
        """Constructs a new datastore associated with the file location in the current directory specified by
        filepath. Ensure the """
        self._file_name = file_name
        self._data = None
        self._shutdown = True

    def __del__(self):
        """Ensures the autosave loop ceases upon shutdown"""
        self._shutdown = True

    def get_data(self):
        """Returns the data"""
        return self._data

    def set_data(self, obj):
        """Sets the data"""
        self._data = obj

    def get_file_name(self):
        """Returns the filename"""
        return self._file_name

    def load(self):
        """Loads the data from the file storage location"""
        with open(self._file_name, 'r') as f:
            obj = jsonpickle.decode(f.read())
            self._data = obj

    def save(self):
        """Saves the data to the file storage location"""
        with open(self._file_name, 'w') as f:
            f.write(jsonpickle.encode(self._data))

    def start_autosave(self, timeout=10):
        """Begins the autosave loop which saves the data at a specified interval.
        timeout:param the time elapsed in seconds between autosaves"""
        self._shutdown = False
        Thread(target=self._autosave_loop, args=(timeout,)).start()

    def stop_autosave(self):
        """Ceases the autosave loop"""
        self._shutdown = True

    def _autosave_loop(self, timeout):
        while not self._shutdown:
            self.save()
            Event().wait(timeout=timeout)