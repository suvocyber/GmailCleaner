from Google import Create_Service
from pprint import pprint


CLIENT_FILE = 'client.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

s = Create_Service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)


class GClean:
    def __init__(self, service):
        self.service = service


    def search_mail(self, searchparam):
        tobedeleted = []
        nextPageToken = None
        while True:
            tobedeleted.clear()
            msg_results = self.service.users().messages().list (userId='me', pageToken=nextPageToken, q=searchparam,
                                                                  labelIds=['INBOX']).execute()
            if msg_results.get ('nextPageToken') != None:
                nextPageToken = msg_results['nextPageToken']

                msg = msg_results.get('messages')
                for i in msg:
                    content = self.service.users().messages().get(userId='me', id=i.get('id')).execute()
                    print(content.get('snippet')[:100])
                    g = content.get('id')
                    tobedeleted.append(g)
            elif msg_results.get('nextPageToken') is None:
                msg = msg_results.get ('messages')
                if msg is None:
                    print("No Messages Found!")
                    break
                else:
                    for i in msg:
                        content = self.service.users ().messages ().get (userId='me', id=i.get ('id')).execute ()
                        #print(content.get('snippet')[:100])
                        g = content.get('id')
                        tobedeleted.append(g)
                break
            else:
                break
        return tobedeleted

    def execute_deletion(self, deletes):
        for i in deletes:
            self.service.users().messages().delete(userId='me', id=i).execute()
        print(f'All {len(deletes)} messages have been deleted.')

    def show_mail(self, searched):
            snippets = []
            for i in searched:
                content = self.service.users().messages().get(userId='me', id=i).execute()
                #print(content.get('snippet')[:100])
                snippets.append(content.get('snippet'))
            return snippets





















#nextPageToken = None
#total_msg = 0
#while True:
#    msg_results = service.users().messages().list(userId='me', pageToken=nextPageToken, labelIds=['INBOX']).execute()
#    if (msg_results.get('nextPageToken') != None):
#        nextPageToken = msg_results['nextPageToken']
#        #result_size = msg_results.get('resultSizeEstimate')
#        #total_msg += result_size
#        #print(f'{result_size} in this call.')
#        msg = msg_results.get ('messages')
#        for i in msg:
#            #pprint(i.get('id'))
#            a_message = service.users().messages().get(userId='me', id=i.get('id')).execute()
#            #pprint(a_message.get('id'))
#            #pprint(a_message.get('snippet'))
#            t = a_message['snippet']
#            #pprint((t)[:40])
##
#            if t.find('The Hacker News') != -1:
#                iden = a_message.get ('id')
#                print(f"MessageID: {iden}, {t[:40]} Matched, and Deleted!")
#                service.users().messages().delete(userId='me', id=iden).execute()
###
#            else:
#                #pass
#                print ('Not Matched!')
#
#
#    elif(msg_results.get('nextPageToken') is None):
#        result_size = msg_results.get('resultSizeEstimate')
#        total_msg += result_size
#        print(f'{result_size} messages found in this call.')
#        msg = msg_results.get('messages')
#        for i in msg:
#            pprint(i.get('id'))
#            a_message = service.users().messages().get(userId='me', id=i.get('id')).execute()
#            #pprint(a_message.get('id'))
#            #pprint(a_message.get('snippet'))
#            t = a_message['snippet']
#            #pprint((t)[:20])
#            #if t.find('The Hacker News') != -1:
###
#            #    iden = a_message.get ('id')
#            #    print(f"MessageID: {iden}, {(t)[:40]} | Matched, and Deleted!")
#            #    service.users().messages().delete(userId='me', id=iden).execute()
###
#            #else:
#            #    #pass
#            #    print('Not Matched!')
#        break
#    else:
#        break
#
#
##print(f'In Total you have {total_msg} messages approximately!')

t1 = GClean(s)
print('Called Search mail!')
num = t1.search_mail('from:suvocyber@gmail.com')
print(f'We have found {len(num)} email, which can be deleted!')

print('Called show_mail')
total = t1.show_mail(num)
for x in total:
    print(x)


print('Called delete_emails')
t1.execute_deletion(num)





#t1.search_mail(None)
#print(f'mails from {t1}.')
#
#print('_____________________________________________________________________________________')
#
#t2 = GClean(s)
#t2.search_mail(None)
#print(f'mails from {t2}.')