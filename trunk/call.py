import telephone,e32
class call:
    """This module attemps to manage incoming calls and answer"""
    def __init__(self):
        print "se invocó llamada"

    def cb_calling(state):
        if (state[0]==telephone.EStatusRinging):
            return "Estás recibiendo una llamada"
        elif(state[0]==telephone.EStatusDialling):
            return "Estás haciendo una llamada"



