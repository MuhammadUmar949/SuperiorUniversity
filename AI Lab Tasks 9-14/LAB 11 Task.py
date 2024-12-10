from sklearn.preprocessing import StandardScaler

data.fillna(data.mean(), inplace=True)
for col in data.select_dtypes(include='object').columns:
    data[col] = data[col].astype('category').cat.codes
scaler = StandardScaler()
features = data.iloc[:, :-1]
target = data.iloc[:, -1]
scaled_features = scaler.fit_transform(features)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(scaled_features, target, test_size=0.3, random_state=42)

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
svm_model = SVC(kernel='linear', C=1.0, random_state=42)
svm_model.fit(X_train, y_train)
y_pred = svm_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
