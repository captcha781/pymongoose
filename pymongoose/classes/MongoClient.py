import pymongo as pm


class MongooseClient:
    def __init__(self, data_store):
        self.data_store = ""
        if type(data_store) is str:
            if len(data_store) == 0:
                raise ValueError("connection string cannot be empty")
            self.uri = data_store
        elif type(data_store) is pm.MongoClient:
            self.data_store = data_store
        else:
            raise TypeError(f"Invalid connection string {data_store}")

    def connection(self):
        self.data_store = pm.MongoClient(self.uri)

    @classmethod
    def connect_via_external(cls, uri):
        client = pm.MongoClient(uri)
        cls(client)
