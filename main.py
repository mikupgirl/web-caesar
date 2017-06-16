from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """ <!DOCTYPE html>

<html>
    <head>
        <style>
           form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;                
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;               
            }}
        </style>
    </head>
    <body>

                <form method="POST">
                    <label>
                       Rotate By:
                    </label>
                    <input type="text" name="rot" value="0" />
                    <textarea type="text" name="text">{0}</textarea>
                    <input type="submit" value="Submit Query" />
                </form>      
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rotated_text = ''
    user_num = request.form['rot']
    user_text = request.form['text']
    user_num = int(user_num)
    rotated_text = rotate_string(user_text, user_num)
    final_rotated_text = rotated_text
    content = str(final_rotated_text)

    return form.format(content)

@app.route("/")
def index():
    return form.format('')

app.run()