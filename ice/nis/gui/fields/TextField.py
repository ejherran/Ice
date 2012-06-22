'''
Created on 21/06/2012

@author: zero
'''

class TextField():
    
    def __init__(self, value = ""):
        self.value = value
    
    def render(self):
        return "<INPUT TYPE='TEXT' VALUE='"+str(self.value)+"'/>" 