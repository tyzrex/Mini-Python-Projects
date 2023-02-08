from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generate():
    memory = BytesIO() 
    data = request.form['data']
    if not data:
        return render_template('index.html', error='Error: No data entered')
    img = qrcode.make(data)
    img.save(memory, 'PNG')
    memory.seek(0)
    base64_img = "data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii')
    return render_template('index.html', data=base64_img)
    

if __name__ == '__main__':
    app.run(debug=True)    