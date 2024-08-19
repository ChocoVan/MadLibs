# create app and run it

from website.createApp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)