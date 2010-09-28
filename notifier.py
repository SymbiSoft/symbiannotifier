from conection import *
#from preferences import *
#import appuifw,e32
##Just for debbuging needs and execfile because pys60 doesn't see files in the same directory
##with import until make the .sis package
#execfile("E:\\data\\python\\messaging.py")
#execfile("E:\\data\\python\\preferences.py")
#execfile("E:\\data\\python\\conection.py")
#execfile("E:\\data\\python\\call.py") #call manager
#import messaging
#sms=messaging()
#content,contact=sms.last()
#print "Contacto "+contact
#print "Mensaje "+content

#Define the exit function
#[(u"SMS's",'combo',([u'No',u'Yes'],0L)), (u'Calls', 'combo', ([u'No', u'Yes'], 1L)), (u'Battery', 'combo', ([u'No', u'Yes'], 0L)), (u'Other', 'combo', ([u'No', u'Yes'], 0L))]  #LeerNumero

#[(u"SMS's",'combo',([u'No',u'Yes'],0)), (u'Calls', 'combo', ([u'No', u'Yes'], 0)), (u'Battery', 'combo', ([u'No', u'Yes'], 0)), (u'Other', 'combo', ([u'No', u'Yes'], 0))] #Asi debe ser

#---SOCKETS TEST DESKTOP--------------------------------------------
mensaje=conection("v2/10/1/PING/6672100343/Homer")
#mensaje.udp()
mensaje.udp()
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
#import appuifw
#appuifw.app.title=u"Symbian Notifier Preferences"
#class start:
#    def __init__(self):
#        if(self.home()==0):
#            """Formulario de preferencias"""
#            preferencias=preferences()
#            formulario=preferencias.leerArchivo()
#            flags=appuifw.FFormEditModeOnly
#        #   print formulario
#            f=appuifw.Form(formulario,flags)
#            f.execute()
#            preferencias.save(f)
#            self.__init__()
#        else:
#            print "PING"
#            mensaje=conection("v2/10/1/PING/6672100343/Homer")
#            mensaje.udp()
#            self.__init__()
#    def home(self):
#        home = appuifw.selection_list([u'Preferencias',u'Enviar PING'])
#        return home
#
#start()
#--------------------------------------------------------
#---------------------------PICKLE TEST----------------
#import cPickle as pickle
#
#fichero = file("holaa.dat",'w')
#opciones=[u'No',u'Yes']
#test=[(u'SMS\'s','combo',(opciones,0)),(u'Calls','combo',(opciones,0)),(u'Battery','combo',(opciones,0)),(u'Other','combo',(opciones,0))]
#test=("hola","mundo")
#pickle.dump(test,fichero)
#fichero.close()
#fichero = file("holaa.dat")
#testa=pickle.load(fichero)
#print testa
#---------------------------------------------------
#-------------------Pruebas en Localhost----------------
#import socket
#
#ip="localhost"
#port = 10600
#direccion=(ip,port)
#mensaje="v2/10/1/PING/6672100343/Homer"
#conexion=socket.socket()
#conexion.connect(("localhost",10600))
#conexion.sendto(mensaje,direccion)
#conexion.close()
#--------------------------------------------------------