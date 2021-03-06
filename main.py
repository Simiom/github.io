from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    if len(request.args) < 2:
        return render_template('index.html', name="Незнакомец", message="Какими судьбами?")
    else:

        return render_template('index.html', name=request.args['name'], message=request.args['message'])


if __name__ == "__main__":
    app.run()
