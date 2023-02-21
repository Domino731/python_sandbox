# APP: 05
# DATE: 21.02.2023
# Description: create an app for reading email data
# DIRECTORY:
# app.py - main script
# emails.text - text which holding data about e-mails (top 100 from https://email-verify.my-addr.com/list-of-most-popular-email-domains.php)
# test.py - test for app


def create_emails_dict():
    payload = {}
    try:
        f = open("emails.txt", "r")
        # loop though each line and create email dictionary data
        for x in f:
            words_array = x.split()
            email_data = {
                "rank": words_array[0],
                "provider": words_array[1],
                "usage": words_array[2]
            }
            payload.setdefault(words_array[1], email_data)
    except:
        print('An error occurred while trying to read the emails.txt file')
    return payload


EMAILS_DATA = create_emails_dict()


def email_slicer(email):
    if '@' in email:
        index = email.index('@') + 1
        email_length = len(email)
        provider = email[index:email_length]
        user = email[0: index]
        return provider, user
    else:
        return None


def get_email_data(provider):
    if provider in EMAILS_DATA:
        return EMAILS_DATA.get(provider)
    else:
        return None


user_email = email_slicer('domik@gmail.com')
email_data = get_email_data(user_email[0])

if email_data is not None:
    # {'rank': '1', 'provider': 'gmail.com', 'usage': '17.74%'}
    print('Your e-mail')
    print("is " + email_data['rank'] + " in ranking")
    print("provider is " + email_data['provider'])
    print("global usage is " + email_data['usage'])
else:
    print('Error: email not found :(')
