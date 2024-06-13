from sklearn.ensemble import RandomForestClassifier

class Model:
    """Model class for Random Forest."""

    name = "RF"
    version = 0.1

    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=10,
                random_state=42)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
