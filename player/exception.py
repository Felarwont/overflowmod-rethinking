class PlayerAlreadyExist(Exception):
    def __init__(self, account_id: str, message: str = "Player already exist"):
        self.account_id = account_id
        self.message = message
        super().__init__(f"[ERROR] {self.account_id} -- {self.message}")

class PlayerNotFound(Exception):
    def __init__(self, account_id: str, message: str = "Player not found"):
        self.account_id = account_id
        self.message = message
        super().__init__(f"[ERROR] {self.account_id} -- {self.message}")