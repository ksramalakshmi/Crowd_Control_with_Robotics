import eel
from communication import call

eel.init('web')

@eel.expose
def place_call():
    call('+919790590251', 'Hello! Whats up?')  

eel.start('button.html')