import pickle
import json
import numpy as np

with open("./model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("./dataset/time_dict.json", "r") as f:
    time_dict = json.load(f)

with open("./dataset/rate_dict.json", "r") as f:
    rate_dict = json.load(f)

with open("./dataset/diagnose_dict.json", "r") as f:
    diagnose_dict = json.load(f)

yes_or_no = {
    "yes": 1,
    "no": 0,
}


def predict_diagnosis(
    sadness,
    euphoric,
    exhausted,
    sleepdissorder,
    moodSwing,
    suicidalThoughts,
    anorxia,
    authorityRespect,
    tryExplanation,
    aggressiveResponse,
    ignoreMoveOn,
    nervousBreakdown,
    admitMistakes,
    Overthinking,
    sexualActivity,
    concentration,
    optimisim,
):
    # Time
    sadness = time_dict[sadness.lower().strip()]
    euphoric = time_dict[euphoric.lower().strip()]
    exhausted = time_dict[exhausted.lower().strip()]
    sleepdissorder = time_dict[sleepdissorder.lower().strip()]

    # Yes Or No
    moodSwing = yes_or_no[moodSwing.lower().strip()]
    suicidalThoughts = yes_or_no[suicidalThoughts.lower().strip()]
    anorxia = yes_or_no[anorxia.lower().strip()]
    authorityRespect = yes_or_no[authorityRespect.lower().strip()]
    tryExplanation = yes_or_no[tryExplanation.lower().strip()]
    aggressiveResponse = yes_or_no[aggressiveResponse.lower().strip()]
    ignoreMoveOn = yes_or_no[ignoreMoveOn.lower().strip()]
    nervousBreakdown = yes_or_no[nervousBreakdown.lower().strip()]
    admitMistakes = yes_or_no[admitMistakes.lower().strip()]
    Overthinking = yes_or_no[Overthinking.lower().strip()]

    # Rate
    sexualActivity = rate_dict[sexualActivity.lower().strip()]
    concentration = rate_dict[concentration.lower().strip()]
    optimisim = rate_dict[optimisim.lower().strip()]

    features = np.array(
        [
            [
                sadness,
                euphoric,
                exhausted,
                sleepdissorder,
                moodSwing,
                suicidalThoughts,
                anorxia,
                authorityRespect,
                tryExplanation,
                aggressiveResponse,
                ignoreMoveOn,
                nervousBreakdown,
                admitMistakes,
                Overthinking,
                sexualActivity,
                concentration,
                optimisim,
            ]
        ]
    )
    prediction = model.predict(features)

    prediction = diagnose_dict[str(prediction[0])]
    return prediction


print(
    predict_diagnosis(
        "Usually",
        "Seldom",
        "Sometimes",
        "Sometimes",
        "YES",
        "YES ",
        "NO",
        "NO",
        "YES",
        "NO",
        "NO",
        "YES",
        "YES",
        "YES",
        "3 From 10",
        "3 From 10",
        "4 From 10",
    )
)
