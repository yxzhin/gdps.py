

def main():

    from flask import Flask
    import conf.main_config

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    app.run(
        host=conf.main_config.HOST,
        port=conf.main_config.PORT,
        debug=True,
    )


if __name__ == "__main__":
    main()
