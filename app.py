from flask import Flask, render_template, jsonify

flask_app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Chicago, IL, USA',
    'salary': '$120,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Irving, TX, USA',
    'salary': '$150,000'
  },
  {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'Naperville, IL, USA',
    'salary': '$130,000'
  },
  {
    'id': 4,
    'title': 'Talent Acquisition Specialist',
    'location': 'Aurora, IL, USA',
    'salary': '$70,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='VaseWorks')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
