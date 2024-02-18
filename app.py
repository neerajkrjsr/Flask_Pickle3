from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
app = Flask(__name__)
students = pickle.load(open("student_dict.pkl", "rb"))

@app.route("/",methods=['GET'])
def Home():
    return render_template("index.html")

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def GetStudentDetail():
    if request.method == 'POST':
        # getting input with name = Number1 in HTML form
        id = request.form.get("Student_id")
        
        # Test if element is dictionary value using in operator and values()
        id_ok = ("Student " + id) in students.keys()
        
        if (id_ok):
            name = students["Student " + id]["Name"]
            age = students["Student " + id]["Age"]
            grade = students["Student " + id]["Grade"]
            
            return render_template("index.html", Result = "Name: {} --> Age: {} --> grade: {}".format(name, age, grade))
            
        else:
            name = ""
            age = ""
            grade = ""
        
            return render_template('index.html', Result = "")
    else:
        return render_template('index.html', Result = "")

if __name__ == "__main__":
    app.run(debug=True)