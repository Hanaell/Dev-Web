import os
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def page_acceuil():
    return render_template("index.html")

@app.route("/gallery")
def page_gallery():
    return render_template("gallery.html")

@app.route("/gallery_dynamique")
def page_gallery_dynamique():
    chemin_images = os.path.join(app.static_folder, "Images")
    
    extensions_autorisees = ('.jpg', '.jpeg', '.png', '.gif')
    liste_images = [
    f for f in os.listdir(chemin_images)
    if f.lower().endswith(extensions_autorisees)
    ]
    images_urls = [url_for('static', filename=f'Images/{img}') for img in liste_images]

    return render_template('gallery_dynamique.html', images=images_urls)


if __name__ == "__main__":
    app.run(debug=True)