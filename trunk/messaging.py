import inbox, messaging
class messaging:
    """Messaging Interface"""
    def __init__(self):
        i=inbox.Inbox()

    def last(self):
        """Retrieves a tuple of the last message content and contact, in that order"""
        id=i.sms_messages()[0]
        return i.content(id),i.address(id)

    def send(self,number,message,fromautor=null):
        def cb(state):
            if state==messaging.ESent:
                print "**Message was sent**"
            if state==messaging.ESendFailed:
                print "**Something went wrong - Truly sorry for this**"
        messaging.sms_send(number, message, '7bit',cb, fromautor)

