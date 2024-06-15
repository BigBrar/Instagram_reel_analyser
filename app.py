from flask import Flask, request, render_template
import main
import data_extraction

app = Flask(__name__)

@app.route('/')
def main_method():
    return render_template('index.html')

@app.route('/get_user',methods=["POST"])
def user_method():
    if request.method == 'POST':
        print("You are on the right track...")
        username = request.form.get('username')
        html_content = main.main_func(username)
        results = data_extraction.start_extractor(html_content)
        return results