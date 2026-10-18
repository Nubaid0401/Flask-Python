from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("wit.html")

@app.route("/track", methods=["POST"])
def calculate():
    name = request.form["name"]
    goal = int(request.form["goal"])
    glasses = int(request.form["glasses"])

    remaining_amount = goal - glasses

    if glasses >= goal:
        message = f"Congratulations {name}! You've reached your daily water intake goal of {goal}   glasses."
        status = "success"

        remaining_amount = 0

        percentage = 100

    else:
        message = f"Keep going {name}! You have {remaining_amount} glasses left to reach your daily water intake goal of {goal} glasses."
        status = "Goal not reached"

        percentage = (glasses / goal) * 100

    return render_template("wit.html",
                         name=name, 
                         goal=goal, 
                         glasses=glasses, 
                         remaining_amount=remaining_amount, 
                         message=message, 
                         status=status,
                         percentage=percentage)

if __name__ == "__main__":
    app.run(debug=True)