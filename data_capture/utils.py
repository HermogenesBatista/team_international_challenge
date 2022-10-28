from . import DEFAULT_LIMITS
from .exceptions import DataCaptureValueError


def validate_type_and_limit(value, limit=None):
    """
    Validate if type was correct and inside allowed range
    """
    if not limit:
        limit = DEFAULT_LIMITS
    if not isinstance(value, int):
        raise DataCaptureValueError(f"Only integer is allowed. Found: {type(value)}")
    elif value < limit[0] or value > limit[1]:
        raise DataCaptureValueError(f"The values must be between: {limit}")
