import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER


@app.route('/')
@app.route('/home')
def index():
    pass_img= os.path.join(app.config['UPLOAD_FOLDER'], 'password gen.png')
    image_num = os.path.join(app.config['UPLOAD_FOLDER'], 'num_game logo.png')
    image_d = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_2365 copy.jpg')
    image_tic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'tictaccopy.png')
    iconal = os.path.join(app.config['UPLOAD_FOLDER'], 'alien1 copy.png')
    image_t = os.path.join(app.config['UPLOAD_FOLDER'], 'trello.png')
    return render_template("index.html", dani_image=image_d, logo_al=iconal, tic_image=image_tic2, trillo_im=image_t, num_game_image=image_num, password_im=pass_img)


@app.route('/about')
def about():
    image1 = os.path.join(app.config['UPLOAD_FOLDER'], 'FullSizeRender.jpg')
    return render_template("about.html", user_image=image1)



@app.route('/contact')
def contact():
    image10 = os.path.join(app.config['UPLOAD_FOLDER'], 'FullSizeRender.jpg')
    return render_template("contact.html", user_photo=image10)


@app.route('/aliens_guns')
def guns():
    image_al1 = os.path.join(app.config['UPLOAD_FOLDER'], 'alien1.png')
    image_al2 = os.path.join(app.config['UPLOAD_FOLDER'], 'aliens2.png')
    return render_template("aliens_guns.html", alien1=image_al2, alien2=image_al1)


@app.route('/tic_tac')
def tictac():
    image_tic = os.path.join(app.config['UPLOAD_FOLDER'], 'tictac.png')
    return render_template("tic_tac.html", ticpage_image=image_tic)

@app.route('/number_game')
def num_gamer():
    image_nun = os.path.join(app.config['UPLOAD_FOLDER'], 'num_game.png')
    return render_template("numbers_game.html", num_img_image=image_nun)

@app.route('/cinema')
def cinema():
    image_c = os.path.join(app.config['UPLOAD_FOLDER'], 'cinema.png')
    return render_template("cinema tickets.html", cinema_image=image_c)

if __name__ == '__main__':
    app.run(debug=True)


