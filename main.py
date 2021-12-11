from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def test():
    return render_template('/main.html')


@app.route('/', methods=['POST'])
def my_form_post():
    content = request.form['content']
    return content

if __name__ == "__main__":
    app.run()
