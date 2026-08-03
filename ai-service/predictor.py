import random


def predict_defect(filename: str):
    """
    Simulate an AI prediction based on the filename.
    """

    filename = filename.lower()

    if "good" in filename:
        prediction = "Good"
        confidence = round(random.uniform(97, 99.9), 2)

    elif "defect" in filename or "crack" in filename:
        prediction = "Defective"
        confidence = round(random.uniform(95, 99.5), 2)

    else:
        prediction = random.choice(["Good", "Defective"])
        confidence = round(random.uniform(85, 99), 2)

    return {
        "prediction": prediction,
        "confidence": confidence
    }
