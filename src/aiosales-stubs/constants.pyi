from enum import Enum

class DeliveryStatus(str, Enum):
    INITIATED: str
    DONE: str
    CANCELLED: str
    FAILED: str
