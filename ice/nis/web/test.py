'''
Created on 21/06/2012

@author: zero
'''

from ice.nis.gui.containers.Page import Page
from ice.nis.gui.actors.Button import Button
from ice.nis.gui.fields.TextField import TextField

def index(req):
    
    txt = TextField("Caja De Texto");
    btn = Button("Probar Boton")
        
    test = Page("Test Python")
    test.insert("caja", txt)
    test.insert("boton", btn)
    
    return test.render()


print(index("x"))