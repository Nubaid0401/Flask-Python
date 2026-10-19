from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('difference.html')

@app.route('/calculate', methods=['POST'])
def calculate_difference():
    date1 = int(request.form['date1'])
    month1 = request.form['month1']
    date2 = int(request.form['date2'])
    month2 = request.form['month2']

    difference = date2 - date1

    if difference < 0:
        difference = abs(difference)
        message = f"The difference is {difference} days (date2 is earlier than date1). The date is {date1} {month1} and {date2} {month2}."
    else:
        message = f"The difference is {difference} days. The date is {date1} {month1} and {date2} {month2}."

    return render_template('difference.html', 
                           difference=difference, 
                           message=message)

if __name__ == '__main__':
    app.run(debug=True)
