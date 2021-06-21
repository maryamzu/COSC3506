from DataStore import DataStore
from Message import Message


class ServerDataStore(DataStore):

    def __init__(self, file_name = "ServerDataStore.txt"):
        """Constructs a new Server Data Store object whose file path is specified. Filepath
        defaults to 'ServerDataStore.txt'"""
        super().__init__(self, file_name=file_name)
        self.set_data(dict())

    def add_user(self, username, password):
        """Adds a new user with the specified password to the system if that username
        is not already in the system"""
        if username not in list(self.get_data()):
            return False
        self.get_data()[username] = {"username": username,
                                     "password": password,
                                     "status": "ONLINE",
                                     "inbox": [],
                                     "outbox": [],
                                     "number_backlogged": 0}
        return True

    def get_status_info(self):
        """Returns the status of each user in the system as a dictionary of the form
        {username:status, ...}"""
        statuses = dict()
        for user in self.get_data():
            statuses[user] = self.get_data()[user]["status"]

    def post_message(self, m: Message):
        """Adds a message to the data store in the sender's outbox and the recipient's inbox"""
        if self.user_exists(m.sender) and self.user_exists(m.recipient):
            self.get_data()[m.sender]["outbox"].append(m)
            self.get_data()[m.recipient]["inbox"].append(m)
            self.get_data()[m.recipient]["number_backlogged"] += 1
        else:
            raise Exception

    def get_new_messages(self, username):
        """Returns a (possibly empty) list of the new messages destined for the specified user
        which have not yet been fetched"""
        if not self.user_exists(username): raise Exception

        number_backlogged = self.get_data()[username]["number_backlogged"]
        self.get_data()[username]["number_backlogged"] = 0
        inbox = self.get_data()[username]["inbox"]

        if number_backlogged == 0:
            return []
        else:
            return inbox[-number_backlogged:].copy()

    def get_all_data(self, username):
        """Returns all the information contained in the data store about the specified user"""
        if not self.user_exists(username): raise Exception
        return self.get_data()[username].copy()

    def post_status(self, username, status):
        """Sets the specified user's status to the specified status"""
        if not self.user_exists(username): raise Exception
        self.get_data()[username]["stats"] = status

    def authenticate_user(self, username, password):
        """Returns true if and only if there is a user with the specified username and
        password in the system"""
        return self.user_exists(username) and self.get_data()[username]["password"] == password

    def user_exists(self, username):
        """Returns true if and only if there is a record for the specified username in the data store"""
        return username in self.get_data()