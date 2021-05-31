from Google import Create_Service
from pprint import pprint
import json

CLIENT_FILE = 'client.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

nextPageToken = None
total_msg = 0
while True:
    msg_results = service.users().messages().list(userId='me', pageToken=nextPageToken, labelIds=['INBOX']).execute()
    if (msg_results.get('nextPageToken') != None):
        nextPageToken = msg_results['nextPageToken']
        #result_size = msg_results.get('resultSizeEstimate')
        #total_msg += result_size
        #print(f'{result_size} in this call.')
        msg = msg_results.get ('messages')
        for i in msg:
            #pprint(i.get('id'))
            a_message = service.users().messages().get(userId='me', id=i.get('id')).execute()
            #pprint(a_message.get('id'))
            #pprint(a_message.get('snippet'))
            t = a_message['snippet']
            #pprint((t)[:40])
#
            if t.find('Recognized') != -1:
                iden = a_message.get ('id')
                print(f"MessageID: {iden}, {t[:40]} Matched, and Deleted!")
                service.users().messages().delete(userId='me', id=iden).execute()
#
            else:
                pass
                #print ('Not Matched!')


    elif(msg_results.get('nextPageToken') is None):
        result_size = msg_results.get('resultSizeEstimate')
        total_msg += result_size
        print(f'{result_size} messages found in this call.')
        msg = msg_results.get('messages')
        for i in msg:
            pprint(i.get('id'))
            a_message = service.users().messages().get(userId='me', id=i.get('id')).execute()
            #pprint(a_message.get('id'))
            #pprint(a_message.get('snippet'))
            t = a_message['snippet']
            #pprint((t)[:20])
            if t.find('Recognized') != -1:
#
                iden = a_message.get ('id')
                print(f"MessageID: {iden}, {(t)[:40]} | Matched, and Deleted!")
                service.users().messages().delete(userId='me', id=iden).execute()
#
            else:
                pass
                #print('Not Matched!')
        break
    else:
        break


#print(f'In Total you have {total_msg} messages approximately!')