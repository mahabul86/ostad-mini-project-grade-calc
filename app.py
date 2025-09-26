from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def grade_calculator():
    # Get parameters from URL query string, e.g., ?name=John&marks=85
    name = request.args.get("name", default="Student")
    try:
        grade_marks = float(request.args.get("marks", default=0))
    except ValueError:
        return "Enter a valid number for marks ❗"

    # Validate marks
    if grade_marks < 0 or grade_marks > 100:
        return "Enter a valid mark ❗"

    # Determine grade
    result = f"--**-- RESULT --**--\nName: {name}\n"
    if grade_marks >= 80:
        result += "Your grade is: A+ 🎉"
    elif grade_marks >= 70:
        result += "Your grade is: A 🙌"
    elif grade_marks >= 60:
        result += "Your grade is: B 👏"
    elif grade_marks >= 50:
        result += "Your grade is: C 👍"
    elif grade_marks >= 40:
        result += "Your grade is: D 👎"
    else:
        result += "❌ You didn't get pass marks 😢"

    # Return result as plain text
    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(debug=True)