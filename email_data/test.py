from email_data.app import EMAILS_DATA, create_emails_dict, email_slicer, get_email_data

# check if the most popular e-mails are loaded
assert len(EMAILS_DATA.values()) == 100
# check if the create_email_dict function is returning dict
assert type(create_emails_dict()) is dict
# check if the type of EMAILS_DATA is dict
assert type(EMAILS_DATA) is dict
# check if the email_data working correctly
assert email_slicer('randomnone.com') is None
assert email_slicer('random@gmail.com') is not None
assert email_slicer('random@gmail.com')[0] in EMAILS_DATA is not None
# check if the get_email_data working correctly
assert get_email_data('gmail.com') is not None
assert get_email_data('testm') is None
