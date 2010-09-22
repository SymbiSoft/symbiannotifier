import inbox
class messaging:
    """Messaging Interface"""
    def __init__(self):
        i=inbox.Inbox()

    def last(self):
        """Retrieves a tuple of the last message content and contact, in that order"""
        id=i.sms_messages()[0]
        return i.content(id),i.address(id)