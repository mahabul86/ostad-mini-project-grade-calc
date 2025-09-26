import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def grade_calculator():
    name = request.args.get("name", default="Student")
    try:
        grade_marks = float(request.args.get("marks", default=0))
    except ValueError:
        return "Enter a valid number for marks ❗"

    if grade_marks < 0 or grade_marks > 100:
        return "Enter a valid mark ❗"

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

    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides the port
    app.run(host="0.0.0.0", port=port)