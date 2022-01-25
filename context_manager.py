# you should implement context manager that allow to handle connection and while connection is open connection should
# accept values and add it to storage and log errors that
# connection should be closed automatically when we leave with.. block


class Connection:
    def __init__(self):
        self._storage = []
        self._logs = []
        self._is_open = False

    @property
    def is_open(self):
        return self._is_open

    def open(self):
        self._is_open = True

    def close(self):
        self._is_open = False

    def add_item(self, item):
        if self.is_open:
            if isinstance(item, int):
                raise ValueError('Wrong value')
            self._storage.append(item)

    def get_storage(self):
        return self._storage

    def add_log(self, log):
        if self.is_open:
            self._logs.append(log)

    def get_logs(self):
        return self._logs


class ConnectionHandler:
    """your code here"""

    def __init__(self, *args):
        self.connection = None

    def __enter__(self):
        self.connection = Connection()
        self.connection.open()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


# tests
connection = Connection()

with ConnectionHandler(connection) as conn:
    conn.add_item('hi')
    conn.get_storage()
    #conn.add_item(1)

assert not connection.is_open
# The problem that i have met is I have two different variables(conn and connection) and conn has the right length
# but connection has another length and I can't understand why
assert len(connection.get_storage()) == 1
assert len(connection.get_logs()) == 1

print('Success')
