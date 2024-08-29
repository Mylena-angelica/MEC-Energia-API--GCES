import pytest
from utils.email.valid_email import verify_email_is_valid

def test_email_exist_and_valid():
    assert verify_email_is_valid("lucaslopesfrazao2003@gmail.com") == True

def test_email_invalid_format():
    with pytest.raises(Exception):
        verify_email_is_valid("invalid-email")
    with pytest.raises(Exception):
        verify_email_is_valid("invalid@.com")
    with pytest.raises(Exception):
        verify_email_is_valid("invalid@com")
    with pytest.raises(Exception):
        verify_email_is_valid("email@nonexistentdomain12345.com")
    with pytest.raises(Exception):
        verify_email_is_valid("example@domainwithoutmx.com")