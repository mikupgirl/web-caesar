from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route("/")



""" <!DOCTYPE html>

<html>
    <head>
        <style>
           """ form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;                
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;               
            }
            """
        </style>
    </head>
    <body>

        caesar_form = """
            <form method="POST">
                <label>
                    Rotate By:
                </label>
                <input type="text" name="rot"/>
                <input type="textarea" name="text"/>
                <input type="submit" value="Submit Query"/>
            </form>
"""      
        
    </body>
</html>
"""


def index():
    return "Hello World"

app.run()