from flask import Flask, render_template, request

apps = Flask(__name__)

notes = []

@apps.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
        return render_template("home.html", notes=notes)
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    apps.run(debug=True)


