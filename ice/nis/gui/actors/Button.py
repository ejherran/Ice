'''
Created on 21/06/2012

@author: zero
'''

class Button():
    
    def __init__(self, caption):
        self.caption = caption
    
    def render(self):
        return "<BUTTON>"+str(self.caption)+"</BUTTON>"