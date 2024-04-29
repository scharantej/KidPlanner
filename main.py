
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

activities = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        time = request.form.get("time")
        activity_type = request.form.get("activity_type")

        activity = {
            "name": name,
            "time": time,
            "activity_type": activity_type
        }

        activities.append(activity)

        return redirect(url_for("index"))

    return render_template("index.html", activities=activities)

@app.route("/schedule", methods=["GET"])
def schedule():
    return render_template("schedule.html", activities=activities)

if __name__ == "__main__":
    app.run(debug=True)
