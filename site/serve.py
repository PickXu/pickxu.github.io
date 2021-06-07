from flask import Flask
from flask import render_template
from cmsc23200 import course

# Serve the site dynamically.  Mainly for development.

app = Flask(__name__)
app.jinja_env.line_statement_prefix = '%'

@app.route("/")
def overview():
    return render_template('overview.html', course=course)

@app.route("/schedule.html")
def schedule():
    return render_template('schedule.html', course=course)

@app.route("/assignments.html")
def assignments():
    return render_template('assignments.html', course=course)

@app.route("/phoenixforge.html")
def phoenixforge():
    return render_template('phoenixforge.html', course=course)

# @app.route("/project1.html")
# def project1():
#     return render_template('project1.html', course=course)
#  
# @app.route("/project2.html")
# def project2():
#     return render_template('project2.html', course=course)
#  
# @app.route("/project3.html")
# def project3():
#     return render_template('project3.html', course=course)
#  
# @app.route("/project4.html")
# def project4():
#     return render_template('project4.html', course=course)
#  
# @app.route("/project5.html")
# def project5():
#     return render_template('project5.html', course=course)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
