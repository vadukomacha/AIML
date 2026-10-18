from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def run(data, features, name):
    df = pd.DataFrame(data)
    x = df.iloc[:, :-1].copy()
    y = df.iloc[:, -1]
    for c in x:
        x[c] = LabelEncoder().fit_transform(x[c].astype(str))
    y = LabelEncoder().fit_transform(y.astype(str))
    m = DecisionTreeClassifier(
        criterion="entropy",
        random_state=42
    ).fit(x, y)
    print("\n", name)
    print(export_text(m, feature_names=features))
    print("Depth:", m.get_depth())
    print("Leaves:", m.get_n_leaves())

#Test Case 1
play_tennis = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]
run(
    play_tennis,
    ["Outlook", "Temperature", "Humidity", "Wind"],
    "Play Tennis Dataset"
)

# Test Case 2
clear_data = [
    ["Red", "Yes"],
    ["Red", "Yes"],
    ["Red", "Yes"],
    ["Blue", "No"],
    ["Blue", "No"],
    ["Blue", "No"]
]
run(
    clear_data,
    ["Color"],
    "Clear Class Separation Dataset"
)

# Test Case 3
mixed_data = [
    [20, "Low", "No"],
    [25, "Low", "No"],
    [30, "Medium", "Yes"],
    [35, "Medium", "Yes"],
    [40, "High", "Yes"],
    [45, "High", "Yes"]
]
run(
    mixed_data,
    ["Age", "Income"],
    "Mixed Attribute Dataset"
)

# Test Case 4
same_class = [
    ["A", "Yes"],
    ["B", "Yes"],
    ["C", "Yes"],
    ["D", "Yes"],
    ["E", "Yes"]
]
run(
    same_class,
    ["Feature"],
    "Same Class Dataset"
)

# Test Case 5
missing_data = [
    ["Sunny", "Hot", "No"],
    ["Rain", "Mild", "Yes"],
    ["Overcast", "Cool", "Yes"],
    [None, "Hot", "No"],
    ["Rain", None, "Yes"]
]
run(
    missing_data,
    ["Outlook", "Temperature"],
    "Missing Attribute Dataset"
)

