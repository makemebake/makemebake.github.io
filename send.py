import requests 

#Creating a mailing list through the API:
def create_mailing_list():
    return requests.post(
        "https://api.mailgun.net/v3/lists",
        auth=('api', 'YOUR_API_KEY'),
        data={'address': 'LIST@YOUR_DOMAIN_NAME',
              'description': "Mailgun developers list"})



#sending mail
def send_simple_message():
    return requests.post(


        "https://api.mailgun.net/v3/sandbox2e967ec2442f418c871db79bae2759d2.mailgun.org/messages",
        auth=("api", "key-f7814ba6ada379e237f656d4dd040646"),
        data={"from": "Excited User <mailgun@sandbox2e967ec2442f418c871db79bae2759d2.mailgun.org>",
              "to": [ "sophieraju@hotmail.co.uk",
              "subject" "Makemebake newsletter!",
              "text" "file:///Users/sophieraju/Documents/Myapp/templates/newsletter1.html"
              "html" "<html> </html> "