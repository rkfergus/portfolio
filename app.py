from flask import Flask, render_template, send_file
from flask_bootstrap import Bootstrap
import plotly.express as px
from pandas.api.types import CategoricalDtype

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
    print(df.describe())

    avgs = wg.get_average_by_day()
    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun',]
    avgs = avgs.reindex(days)
    avgs.loc['Avg'] = avgs.describe().loc['mean']
    print(avgs)

    fig = px.bar(x=avgs.index, y=avgs['Tip '], color=avgs['Tip '], color_continuous_scale='sunsetdark')
    fig.update_layout(
        title="Average Tips per Day",
        title_x=0.5,
        xaxis_title="Day",
        yaxis_title="Avg. Tip",
        paper_bgcolor='rgb(0,0,0,0)',
        plot_bgcolor='rgba(231, 231, 231, 0.25)',
        yaxis_tickprefix='$', yaxis_tickformat=',.2f',
        yaxis_ticklabelposition='outside',
    )

    return render_template('wages.html', plot=fig.to_html())


if __name__ == '__main__':
    app.run()
