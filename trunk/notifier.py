import appuifw,e32
#Just for debbuging needs and execfile because pys60 doesn't see files in the same directory
#with import until make the .sis package
execfile("E:\\data\\python\\messaging.py")
execfile("E:\\data\\python\\preferences.py")
#import messaging
#sms=messaging()
#content,contact=sms.last()
#print "Contacto "+contact
#print "Mensaje "+content

#Define the exit function

#The title must be in unicode
appuifw.app.title=u"Symbian Notifier Preferences"
#preferencias=(u'SMS\'s',u'Calls',u'Others')
opciones=[u'Yes',u'No']
preferencias=[(u'SMS\'s','combo',(opciones,0)),(u'Calls','combo',(opciones,1)),(u'Battery','combo',(opciones,1)),(u'Other','combo',(opciones,0))]
flags=appuifw.FFormEditModeOnly
f=appuifw.Form(preferencias,flags)
f.execute()
for campo in f:
    print campo
#preferencias = appuifw.multi_selection_list([u'SMS\'s',u'Calls',u'Others'])
#appuifw.multi_selection_list([u'SMS\'s',u'Calls',u'Others'])
#preferencias=preferences()
#preferencias.save(8)
#print preferencias.leerNumero()

