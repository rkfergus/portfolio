from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap
import re

app = Flask(__name__)
Bootstrap(app)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello_world():
    text_file = 'static/resources/home.txt'
    text_content = open(text_file).readlines()

    print(text_content)

    return render_template('index.html', text=text_content)


@app.route('/projects')
def projects():
    return render_template('projects.html')



@app.route('/links')
def links():
    return render_template('links.html')


@app.route('/wages')
def wages():
    import wages as wg
    df = wg.load()
    print(df)
    return render_template('wages.html', df=df.to_html())

if __name__ == '__main__':
    app.run()
