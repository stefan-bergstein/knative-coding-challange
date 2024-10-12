from flask import Flask, request, make_response
import uuid
import os
from logging.config import dictConfig


log_level = os.getenv("LOG_LEVEL", default="ERROR")

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
            # Set root logger level to DEBUG, INFO, WARNING, ERROR, or CRITICAL
            "level": log_level,
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

    bug = True
    if not bug:
        response = make_response({"msg": "Hi from receiver-python app!"})
        response.headers["Ce-Id"] = str(uuid.uuid4())
        response.headers["Ce-specversion"] = "0.3"
        response.headers["Ce-Source"] = "knative/eventing/samples/receiver"
        response.headers["Ce-Type"] = "dev.knative.samples.hifromknative"
        response.status_code = "200"
    else:
        response = True

    return response


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
