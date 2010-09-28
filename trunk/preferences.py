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
        archivo = file("pe.dat","w",2)
        for element in metalist:
            pickle.dump(element[2][1],archivo)
        archivo.close()

    def leerArchivo(self):
        """Retrieves the preferences data"""
        try:
            import cPickle as pickle
        except ImportError:
            import pickle
        try:
            archivo = file("pe.dat")
            preferencias=[(u'SMS\'s','combo',(opciones,int(pickle.load(archivo)))),(u'Calls','combo',(opciones,int(pickle.load(archivo)))),(u'Battery','combo',(opciones,int(pickle.load(archivo)))),(u'Other','combo',(opciones,int(pickle.load(archivo))))] #0 No, 1 Yes
            archivo.close()
        except EnvironmentError:
            print "No existe archivo"
            preferencias = self.preferencias
        return preferencias


