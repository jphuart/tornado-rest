import tornado.ioloop
import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get

class MyObject(object):
    id_object = int
    name_object = str
    
    def __init__(self,id_object=0, name_object=None):
        self.id_object      = id_object
        self.name_object    = name_object
        return
    
    def __str__(self):
        return '{0} - {1}'.format(self.id_object, self.name_object)

class JsonpService(pyrestful.rest.RestHandler):
    @get(_path="/jsonp/{name}/{callback}", _produces=mediatypes.APPLICATION_JSONP)
    def sayHello(self, name, callback):
        """
        JSONP with defined callback
        """
        return {"Hello":name}
      
    @get(_path="/jsonpwithout/{name}", _produces=mediatypes.APPLICATION_JSONP)
    def sayHelloWithoutCallback(self, name):
        """ 
        JSONP without defining a callback
        Will use the default value for callback
        """
        return {"Hello":name}
    
    @get(_path="/jsonplist/{name1}/{name2}/{callback}", _produces=mediatypes.APPLICATION_JSONP)
    def helloList(self, name1, name2, callback):
        """ 
        JSONP with defined callback
        """
        mylist = [name1, name2]
        
        return mylist
    
    @get(_path="/jsonpobject/{id}/{name}/{callback}", _produces=mediatypes.APPLICATION_JSONP)
    def helloObject(self, id, name, callback):
        """ 
        JSONP with defined callback
        """
        myobject = MyObject(id_object=id, name_object=name)
        
        return {"the object":str(myobject)}

if __name__ == '__main__':
    try:
        print("Start the jsonp service")
        app = pyrestful.rest.RestService([JsonpService])
        app.listen(8080)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStop the jsonp service")
