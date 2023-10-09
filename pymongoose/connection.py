from .classes.MongoClient import MongooseClient as MC

def connection (uri_string: str):
    MC.connect_via_external(uri=uri_string)