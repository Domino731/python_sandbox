# data from https://email-verify.my-addr.com/list-of-most-popular-email-domains.php

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
    print(payload)


create_emails_dict()
