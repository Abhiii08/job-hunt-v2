from flask import Flask, render_template, jsonify

app = Flask("__name__")

Jobs = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Pune, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Banglore, India',
    'salary': 'Rs. 13,00,000'
}, {
    'id': 3,
    'title': 'Frontend developer',
    'location': 'Mumbai, India',
    'salary': 'Rs. 7,50,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Fransisco, USA',
    'salary': '$130,000'
}]


@app.route("/")
def first():
  return render_template("home.html", jobs=Jobs)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(Jobs)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
