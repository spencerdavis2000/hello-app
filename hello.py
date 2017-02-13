from flask import Flask 
import os # for host os.getenv

# create an instance
app = Flask(__name__) # magic method called name

# now define a route 
# the @ sign is called a decorator
# it decorates with a behavior
# what we decorate is the function hello world
@app.route('/')
def hello_world():
    return 'Hello World'
    
# this means it is being called via the terminal
# and not the from the python terminal
if __name__ == '__main__':
    # run creates a server all the time waiting 
    # until somebody hits an address of the application
    # and then route it to correct route
    
    # you need to define a host
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port) 
    
   
   
   
   
   
    