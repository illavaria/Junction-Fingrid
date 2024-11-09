from enum import Enum


class CHANGE_STATUS(Enum):
    requested = 'requested'
    edited = 'edited'
    assigned = 'assigned'
    in_process = 'in_process'
    released = 'released'
