#CONSTANTS
import inspect
URL = "https://www.google.com/"
USERNAME = "Admin"
PASSWORD = "admin123"


def whoami():
    return inspect.stack()[1][3]