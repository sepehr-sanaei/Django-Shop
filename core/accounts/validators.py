import re
from django.core.exceptions import ValidationError

# Validation function for Iranian phone numbers
def validate_iranian_phone_number(value):
    IRANIAN_PHONE_REGEX = r"^(09)[0-9]{9}$"
    if not re.match(IRANIAN_PHONE_REGEX, value):
        raise ValidationError(f"{value} is not a valid Iranian phone number.")

