from flask import Flask

app = flask(__name__)

@app.route('/')
def main():
    return 'meu site em flask :D'

if __name__ == '__main__':
    app.run(debug=True)