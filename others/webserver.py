from flask import Flask,request
import os

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    """if request.method == 'POST':
       data = request.get_json()
       challenge= data.challenge
       """
   # os.startfile('twitch_send.py')
    return ('Imundisse disse')



def run():
    port = int(os.environ.get('PORT'))
    app.run(port=port)

if __name__ == '__main__':
    run()
