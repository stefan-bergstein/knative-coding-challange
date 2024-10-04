from flask import Flask, request, make_response
import uuid

from logging.config import dictConfig

# Configure logging using dictConfig
dictConfig(
    {
        # Specify the logging configuration version
        "version": 1,
        "formatters": {
            # Define a formatter named 'default'
            "default": {
                # Specify log message format
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            # Define a console handler configuration
            "console": {
                # Use StreamHandler to log to stdout
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                # Use 'default' formatter for this handler
                "formatter": "default",
            }
        },
        # Configure the root logger
        "root": {
            # Set root logger level to CRITICAL
            "level": "CRITICAL",
            # Attach 'console' handler to the root logger
            "handlers": ["console"],
        },
    }
)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    app.logger.warning(request.data)
    print("Received event: {}".format(request.data))
    # Respond with another event (optional)

    # response = make_response({"msg": "Hi from helloworld-python app!"})
    # response.headers["Ce-Id"] = str(uuid.uuid4())
    # response.headers["Ce-specversion"] = "0.3"
    # response.headers["Ce-Source"] = "knative/eventing/samples/hello-world"
    # response.headers["Ce-Type"] = "dev.knative.samples.hifromknative"
    # return response
    return


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
