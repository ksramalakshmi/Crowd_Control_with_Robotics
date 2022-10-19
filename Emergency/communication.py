from twilio.rest import Client

account_sid = 'AC630da0d5ae6b0071f89db5707d5191f1'
auth_token = '09107c328a3f4c81c7d00694a4fcba3c'
client = Client(account_sid, auth_token)

def call(number, msg):
    call = client.calls.create(
                            twiml='<Response><Say>'+msg+'</Say></Response>',
                            to=number ,
                from_= '+18706148173'
                        )
                      