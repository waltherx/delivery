import os
from delivery import app

#app.secret_key = os.urandom(12)
app.run(debug = True, port = 8080)