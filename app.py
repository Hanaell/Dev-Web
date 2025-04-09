from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def page_acceuil():
    return render_template("index.html")

@app.route("/gallery")
def page_gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)