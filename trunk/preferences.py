class preferences:
    """This module will save the user preferences into a database"""
    def __init__(self):
        try:
            import cPickle as pickle
        except ImportError:
            import pickle

    def save(self,numero):
        """Saves a number"""
        try:
            import cPickle as pickle
        except ImportError:
            import pickle
        archivo = file("notifierpref.dat","w",2)
        pickle.dump(numero,archivo)
        archivo.close()

    def leerNumero(self):
        """Retrieves the preferences data"""
        try:
            import cPickle as pickle
        except ImportError:
            import pickle
        archivo = file("notifierpref.dat")
        numero=pickle.load(archivo)
        return numero


