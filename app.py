from flask import Flask, render_template, request
import predict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def predict_home_price():
    result = None
    error = None
    try:
        if request.method == "POST":
            sadness = request.form["sadness"]
            euphoric = request.form["euphoric"]
            exhausted = request.form["exhausted"]
            sleep_disorder = request.form["sleep-disorder"]
            mood_swing = request.form["mood_swing"]
            suicidal_thoughts = request.form["suicidal_thoughts"]
            anorexia = request.form["anorexia"]
            authority_respect = request.form["authority_respect"]
            try_explanation = request.form["try_explanation"]
            aggressive_response = request.form["aggressive_response"]
            ignore_move_on = request.form["ignore_move_on"]
            nervous_breakdown = request.form["nervous_breakdown"]
            admit_mistakes = request.form["admit_mistakes"]
            overthinking = request.form["overthinking"]
            sexual_activity = request.form["sexual-activity"]
            concentration = request.form["concentration"]
            optimism = request.form["optimism"]

            try:
                result = predict.predict_diagnosis(
                    sadness,
                    euphoric,
                    exhausted,
                    sleep_disorder,
                    mood_swing,
                    suicidal_thoughts,
                    anorexia,
                    authority_respect,
                    try_explanation,
                    aggressive_response,
                    ignore_move_on,
                    nervous_breakdown,
                    admit_mistakes,
                    overthinking,
                    sexual_activity,
                    concentration,
                    optimism,
                )
            except Exception as e:
                print(f"Error occurred while predicting diagnosis: {e}")
                error = "An error occurred while predicting diagnosis.Please try again later."
    except Exception as e:
        print(e)
        error = "Fields Don't be Null"
    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    print("Starting Python Flask Server...")
    app.run(debug=True)
