class Logger:

    def __init__(self):
        self.logging_table={}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logging_table:
            self.logging_table[message]=timestamp
            return True
        else:
            if self.logging_table[message]+10<=timestamp:
                self.logging_table[message]=timestamp
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)