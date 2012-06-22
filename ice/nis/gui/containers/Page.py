'''
Created on 21/06/2012

@author: zero
'''

class Page():
    
    body = {}
    
    def __init__(self, title):
        self.title = title
    
    def insert(self, key, elem):
        self.body[key] = elem
    
    def render(self):
        code = "<HTML><HEAD><TITLE>"+str(self.title)+"</TITLE></HEAD>"
        
        code += "<BODY>"
        
        try:
            for i in self.body.keys():
                code += self.body[i].render()
        except:
            code += "Render Error Code 001"
        
        code += "</BODY></HTML>"
        
        return code