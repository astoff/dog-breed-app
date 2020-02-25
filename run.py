import tempfile
from flask import Flask
from flask import render_template, request
from dog_app import which_breed

app = Flask(__name__)

# Index webpage.  It just runs the function `which_breed` to the
# supplied image, and allows the user to select a new image to
# analyze.
@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    try:
        file = request.files['file']
        tmpfile = tempfile.NamedTemporaryFile()
        tmpfile.write(file.read())
        breed = which_breed(tmpfile.name)
        return render_template('master.html', result=breed)
    except:
        return render_template('master.html')

def main():
    app.run(host='0.0.0.0', port=3001, debug=False, threaded=False)

if __name__ == '__main__':
    main()
