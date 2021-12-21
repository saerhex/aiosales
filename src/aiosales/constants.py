from enum import Enum


class DeliveryStatus(str, Enum):
    INITIATED = "INITIATED"
    DONE = "DONE"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
