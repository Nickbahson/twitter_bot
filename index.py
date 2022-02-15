import concurrent.futures

from dotenv import load_dotenv

load_dotenv()

from twitter import tweeterSteamListener

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>A twitter bot!!</p>"


if __name__ == "__main__":
    # app.run()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        p0 = executor.submit(tweeterSteamListener.filter, track=["iphone"])
        p1 = executor.submit(tweeterSteamListener.filter, track=["samsung"])
        p2 = executor.submit(tweeterSteamListener.filter, follow=["1402065949"])
        p3 = executor.submit(tweeterSteamListener.filter, follow=["1134582339311493120"])
        results = [p0, p1, p2, p3]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
