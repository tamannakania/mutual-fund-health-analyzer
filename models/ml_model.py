import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import mean_absolute_error

from sklearn.preprocessing import LabelEncoder


def train_model(df):

    # CLEAN COLUMNS
    df.columns = df.columns.str.strip()

    # ---------------------------
    # LOGISTIC REGRESSION
    # ---------------------------

    X_classification = df[[
        "Investment",
        "Return",
        "Risk"
    ]]

    y = df["Quality"]

    encoder = LabelEncoder()

    y_encoded = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X_classification,
        y_encoded,
        test_size=0.2,
        random_state=42
    )

    classification_model = LogisticRegression()

    classification_model.fit(
        X_train,
        y_train
    )

    predictions = classification_model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    report = classification_report(
        y_test,
        predictions
    )

    # ---------------------------
    # LINEAR REGRESSION
    # PREDICT FUTURE RETURN
    # ---------------------------

    X_regression = df[[
        "Investment",
        "Risk"
    ]]

    y_regression = df["Return"]

    Xr_train, Xr_test, yr_train, yr_test = train_test_split(
        X_regression,
        y_regression,
        test_size=0.2,
        random_state=42
    )

    regression_model = LinearRegression()

    regression_model.fit(
        Xr_train,
        yr_train
    )

    return_predictions = regression_model.predict(
        Xr_test
    )

    mae = mean_absolute_error(
        yr_test,
        return_predictions
    )

    return (
        classification_model,
        accuracy,
        report,
        encoder,
        regression_model,
        mae
    )