import joblib
import pandas as pd

input_cols=["age",
            "bmi",
            "children",
            "smoker",
            "sex",
            "region"]

numeric_cols=["age",
            "bmi",
            "children"]

categorical_cols=["smoker",
                  "sex",
                 "region"]

def charges(
  age,
  bmi,
  children,
  smoker,
  sex,
  region
):
  
  
  best_rf=joblib.load("medical_charges.pkl")
  encoder=joblib.load("encoder.pkl")
  
  test_df=pd.DataFrame(
    {
      "age":[age],
      "bmi":[bmi],
      "children":[children],
      "smoker":[smoker],
      "sex":[sex],
      "region":[region]
    }
  )
  
  test_df[numeric_cols]=test_df[numeric_cols]
  
  encoded_cols=list(encoder.get_feature_names_out(categorical_cols))
  test_df[encoded_cols]=encoder.transform(test_df[categorical_cols])
  
  X_test=test_df[numeric_cols+encoded_cols]
  
  charges_prediction=best_rf.predict(X_test)[0]

  return {
    "charges_prediction":charges_prediction
  }

result=charges(
  age=30,
  bmi=32.5,
  children=0,
  smoker="yes",
  sex="female",
  region="northwest"
)

print(f"Charges Prediction: {result['charges_prediction']}")
  