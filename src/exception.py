import sys 
from types import ModuleType

# try:
from src.logger import logging
# except ImportError:
#     # A fallback logger for when src.logger is not available
#     import logging as logging_fallback
#     logging = logging_fallback
#     logging.basicConfig(level=logging.INFO)

def error_message_detail(error: Exception, error_detail: ModuleType) -> str:
    """
    Creates a detailed error message including file name, line number and error description.
    
    Args:
        error (Exception): The error that occurred
        error_detail (sys): System information about the error
    
    Returns:
        str: Formatted error message
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message[{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: ModuleType):
        """
        Custom exception class with detailed error information.
        
        Args:
            error_message (Exception): The error message
            error_detail (sys): System information about the error
        """
        self.message = error_message
        super().__init__(self.message)
        temp_exception = Exception(error_message)
        self.error_message = error_message_detail(temp_exception, error_detail=error_detail)
    
    def __str__(self) -> str:
        return self.error_message
if __name__=="__main__":
    try :
        a=1/0
    except Exception as e:
        logging.info("Custom Exception has been raised")
        raise CustomException(str(e), sys) from e
# import sys
# import logging
# from types import ModuleType

# # Configure basic logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def error_message_detail(error: Exception, error_detail: ModuleType) -> str:
#     """
#     Creates a detailed error message including file name, line number and error description.
    
#     Args:
#         error (Exception): The error that occurred
#         error_detail (sys): System information about the error
    
#     Returns:
#         str: Formatted error message
#     """
#     _, _, exc_tb = error_detail.exc_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename
#     error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message[{str(error)}]"
#     return error_message

# class CustomException(Exception):
#     def __init__(self, error_message: Exception, error_detail: ModuleType):
#         """
#         Custom exception class with detailed error information.
        
#         Args:
#             error_message (Exception): The error message
#             error_detail (sys): System information about the error
#         """
#         self.message = error_message
#         super().__init__(self.message)
#         self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
#     def __str__(self) -> str:
#         return self.error_message

# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Custom Exception has been raised")
#         raise CustomException(e, sys)