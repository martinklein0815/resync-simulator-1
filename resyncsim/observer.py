"""observer.py: A collection of utils for implementing the Observer pattern.

See: http://en.wikipedia.org/wiki/Observer_pattern

"""

__author__      = "Bernhard Haslhofer"
__copyright__   = "Copyright 2012, ResourceSync.org"

class Observer(object):
    """Observers are informed about events"""
    
    def name(self):
        return self.__class__.__name__
    
    def notify(self, event):
        pass


class Observable(object):
    """Observable subjects issue events and nofiy registered Observers"""
    
    def __init__(self):
        self.observers = []
    
    def register_observer(self, observer):
        """Registers a given observer"""
        print "*** Registering observer: %s ***\n" % observer.name()
        self.observers.append(observer)
        
    def notify_observers(self, event):
        """Notifies observers about change events"""
        for observer in self.observers:
            observer.notify(event)
        