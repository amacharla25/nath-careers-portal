from flask import Flask,render_template

app = Flask(__name__)

JOBS = [
        {
            "job_id": 1,
            "job_title": "Software Engineer",
            "job_location": "San Francisco, CA",
            "salary_amount": 120000
        },
        {
            "job_id": 2,
            "job_title": "Data Analyst",
            "job_location": "New York, NY",
            "salary_amount": 90000
        },
        {
            "job_id": 3,
            "job_title": "Product Manager",
            "job_location": "Seattle, WA",
            "salary_amount": 130000
        }
    ]






@app.route("/") #route is the part of the url - its a decorator
def hello():
    return render_template("home.html", jobs= JOBS, company_name= 'NOSPL')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)
    