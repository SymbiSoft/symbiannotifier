#from conection import *
#from preferences import *
#import appuifw,e32
##Just for debbuging needs and execfile because pys60 doesn't see files in the same directory
##with import until make the .sis package
#execfile("E:\\data\\python\\messaging.py")
execfile("E:\\data\\python\\preferences.py")
#execfile("E:\\data\\python\\conection.py")
#execfile("E:\\data\\python\\call.py") #call manager
#import messaging
#sms=messaging()
#content,contact=sms.last()
#print "Contacto "+contact
#print "Mensaje "+content

#Define the exit function



#---SOCKETS TEST DESKTOP--------------------------------------------
#mensaje=conection("v2/10/1/PING/6672100343/Homer")
#mensaje.udp()
#mensaje.tcp()
#-----------------------------------------------
#--------detecting incoming calls--------------------
#Copyright (c) 2008 Pankaj Nathani
#Waiting for a call
#call=call()
#print call.cb_calling
#telephone.call_state(cb_calling)
##telephone.incoming_call()
#
#app_lock.wait()

#----------------------------------------------------
#----------------Detecting a message entry-----------------------------
#import inbox
#id=0
#def cb(id_cb):
#    global id
#    id=id_cb
#
#i=inbox.Inbox()
#i.bind(cb)
## Send an SMS to your inbox here. The "id" gets updated
#i.address(id)
#i.content(id)

#---------------------------------------------------------------
#---------------------------User Interface----------------------
import appuifw
appuifw.app.title=u"Symbian Notifier Preferences"
home = appuifw.selection_list([u'Preferencias',u'Enviar PING'])
if(home==0):
    """Formulario de preferencias"""
    preferencias=preferences()
    formulario=preferencias.leerNumero()
    flags=appuifw.FFormEditModeOnly
    f=appuifw.Form(formulario,flags)
    f.execute()
    preferencias.save(f)
else:
    print "PING"

#preferencias = appuifw.multi_selection_list([u'SMS\'s',u'Calls',u'Others'])
#appuifw.multi_selection_list([u'SMS\'s',u'Calls',u'Others'])
#preferencias=preferences()
#preferencias.save(8)
#print preferencias.leerNumero()
#--------------------------------------------------------