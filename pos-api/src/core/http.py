class PosException(Exception):
    def __init__(self, name: str, message: str, code: int):
        self.name = name
        self.message = message
        self.code = code