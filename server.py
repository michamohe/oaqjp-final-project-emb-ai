"""Flask server for the Emotion Detection web application.

This module provides two routes:
- "/" renders the main HTML page.
- "/emotionDetector" accepts user text, runs emotion detection, and returns a formatted response.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

APP_NAME = "Emotion Detection App"
INVALID_TEXT_MESSAGE = "Invalid text! Please try again!"


app = Flask(APP_NAME)


@app.route("/")
def render_index_page():
    """Render the application's home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_route():
    """Handle emotion detection requests from the web UI.

    The input text is received from the HTML form field named 'textToAnalyze'.
    If the detected dominant emotion is None, an error message is returned.

    Returns:
        str: A formatted response string for the UI.
    """
    text_to_analyze = request.form.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return INVALID_TEXT_MESSAGE

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


def main():
    """Run the Flask development server on port 5000."""
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
