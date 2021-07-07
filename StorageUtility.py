
from threading import Thread, Event
import jsonpickle


class StorageUtility:

    def __init__(self, filename: str):
        self.__autosave_on = False
        self.__filename = filename

    def load(self):
        """Returns the object stored in jsonpickle format at the specified filename"""
        data = None
        try:
            with open(self.__filename, 'r') as file:
                text = file.read()
                data = jsonpickle.decode(text)
        except FileNotFoundError:
            data = None
        except IOError as e:
            print(e)
        return data

    def save(self, data):
        """Saves the specified object to the specified file in pickle format"""
        try:
            with open(self.__filename, 'w') as file:
                text = jsonpickle.encode(data)
                file.write(text)
        except IOError as e:
            print(e)

    def start_autosave(self, data, timespan: int = 10):
        """Begins saving the specified data to the specified filename at a regular interval of time,
        specified by the parameter timespan (in seconds)"""
        self.__autosave_on = True
        Thread(target=self.__autosave_loop, args=(data, timespan), daemon=True).start()

    def stop_autosave(self):
        """Stops the execution of the autosave loop"""
        self.__autosave_on = False

    def __autosave_loop(self, data, timespan: int):
        """Saves and then waits the period of time specified by the parameter timespan (seconds)"""
        while self.__autosave_on:
            self.save(data)
            Event().wait(timeout=timespan)

