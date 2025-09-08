import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, errors_detail:sys):
        self.error_message = error_message
        _,_, exc_tb = errors_detail.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return "Error occurred in script name [{0}] line number[{1}] with message[{2}]".format(
        self.filename, self.lineno, str(self.error_message))
        
