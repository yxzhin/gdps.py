

def main():

    from flask import Flask

    import conf.server

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    app.run(
        host=conf.server.HOST,
        port=7373,
        debug=True,
    )


if __name__ == "__main__":
    main()
