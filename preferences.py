import shelve
class preferences:
    """This module will save the user preferences into a database"""
    def __init__(self):
        opciones=[u'No',u'Yes']
        self.preferencias=[(u'SMS\'s','combo',(opciones,0)),(u'Calls','combo',(opciones,0)),(u'Battery','combo',(opciones,0)),(u'Other','combo',(opciones,0))] #0 No, 1 Yes
        try:
            import cPickle as pickle
        except ImportError:
            import pickle

    def save(self,metalist):
        """Saves a number"""
        try:
            import cPickle as pickle
        except ImportError:
            import pickle
        archivo = file("notfierprf.dat","w",2)

        for element in metalist:
            pickle.dump(element,archivo)
        archivo.close()

    def leerNumero(self):
        """Retrieves the preferences data"""
        try:
            import cPickle as pickle
        except ImportError:
            import pickle
        try:
            archivo = file("notfierprf.dat")
            for i in range(3):
                preferencias=pickle.load(archivo)
        except EnvironmentError:
            print "No existe archivo"
            preferencias = self.preferencias
        return preferencias


