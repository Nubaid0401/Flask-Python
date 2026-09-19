from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('vowelnum.html')

@app.route('/vowelnum', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST' and 'input_string' in request.form:
        input_string = request.form.get('input_string', '')
        number_of_vowels = 0

        if input_string:
            input_string = input_string.lower()
            for i in input_string:
                if i in 'aeiou':
                    number_of_vowels += 1

        return render_template('vowelnum.html', vowel_count=number_of_vowels)

    return render_template('vowelnum.html')


if __name__ == '__main__':
    app.run(debug=True)
