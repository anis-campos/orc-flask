from flask import Flask, render_template, url_for, request

from . import config

app = Flask(__name__)

app.config.from_object(config)


@app.route('/')
@app.route('/index/')
def index():
    description = """
         Toi, tu n'as pas peur d'être seul ! Les grands espaces et les aventures sont faits pour toi. D'ailleurs, Koh Lanta est ton émission préférée ! Bientôt tu partiras les cheveux au vent sur ton radeau. Tu es aussi un idéaliste chevronné. Quelle chance !
     """
    page_title = "Le test ultime"
    og_url = url_for('index', _external=True)
    og_image = url_for('static', filename='tmp/sample.jpg')
    og_description = "Découvre qui tu es vraiment en faisant le test ultime !"
    return render_template('index.html',
                           user_name='Julio',
                           user_image=url_for('static', filename='img/profile.png'),
                           description=description,
                           og_url=og_url,
                           page_title=page_title,
                           og_image=og_image,
                           og_description=og_description,
                           blur=True)


@app.route('/result/')
def result():
    from .utils import find_content
    gender = request.args.get('gender')
    description = find_content(gender)
    user_name = request.args.get('first_name')
    uid = request.args.get('id')
    profile_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
    return render_template('result.html',
                           user_name=user_name,
                           user_image=profile_pic,
                           description=description)


@app.route('/content/<int:content_id>/')
def content(content_id: int):
    return '%s' % content_id


if __name__ == "__main__":
    app.run()
