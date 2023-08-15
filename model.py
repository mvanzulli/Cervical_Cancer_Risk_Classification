import pandas as pd
from joblib import load

def age_cat(age: int):
    """
    Categorizes a given age into age groups.

    This function takes an integer input representing age and categorizes it into specific age groups 
    which represent decades: <12, <20, <30, <40, <50, <60, <70, >=70 and returns a string representation
    of the age group as follows: "0", "10", "20", "30", "40", "50", "60", "70".

    Args:
        age (int): The age that needs to be categorized into an age group.

    Returns:
        str: The age group the input age belongs to.
    """
    if age < 12:
        return "0"
    elif age < 20:
        return "10"
    elif age < 30:
        return "20"
    elif age < 40:
        return "30"
    elif age < 50:
        return "40"
    elif age < 60:
        return "50"
    elif age < 70:
        return "60"
    else:
        return "70"

def infer_new_prediction(data:pd.DataFrame, model):
    """
    Function to predict based on a new input dataframe.
    :param data: A pandas DataFrame that includes all the necessary features.
    :param model: The trained model that will be used to make the prediction.
    :return: The predicted class.
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input data must be a pandas DataFrame")
        
    # Add target feature
    data["Age_category"] = data["Age"].apply(age_cat)
    data["Smoke (packages)"] = data["Smokes (years)"] * data["Smokes (packs/year)"]

   
    input_features = ['Age', 'Number of sexual partners', 'First sexual intercourse', 'Num of pregnancies', 'Smokes', 'Smokes (years)', 'Smokes (packs/year)', 
                      'Hormonal Contraceptives', 'Hormonal Contraceptives (years)', 'IUD', 'IUD (years)', 'STDs', 'STDs (number)', 'STDs:condylomatosis', 'STDs:cervical condylomatosis', 
                      'STDs:vaginal condylomatosis', 'STDs:vulvo-perineal condylomatosis', 'STDs:syphilis', 'STDs:pelvic inflammatory disease', 'STDs:genital herpes', 'STDs:molluscum contagiosum', 
                      'STDs:AIDS', 'STDs:HIV', 'STDs:Hepatitis B', 'STDs:HPV', 'STDs: Number of diagnosis', 'Dx:Cancer', 'Dx:CIN', 'Dx:HPV', 'Dx', 'Age_category', 'Smoke (packages)']

    if set(input_features) != set(data.columns):
        print("Input features: ", input_features)
        print("Data columns: ", data.columns)
        raise ValueError("Input features must match the model features")
    
    X = data[input_features]
   
    return  model.predict(X)


def infer_output_df(data:pd.DataFrame, infer_model_function=infer_new_prediction):
    
    # Load the models
    biopsy_model = load('selected_Biopsy_model.joblib')
    hinselman_model = load('selected_Hinselmann_model.joblib')
    schiller_model = load('selected_Schiller_model.joblib')
    citology_model = load('selected_Citology_model.joblib')
    any_positive_model = load('selected_any_positive_model.joblib')


    biopsy_prediction = infer_model_function(data, biopsy_model)
    biopsy_bools = biopsy_prediction > 0
    
    hinselman_prediction = infer_model_function(data, hinselman_model)
    hinselman_bools = hinselman_prediction > 0
    
    schiller_prediction = infer_model_function(data, schiller_model)
    schiller_bools = schiller_prediction > 0

    citology_prediction = infer_model_function(data, citology_model)
    citology_bools = citology_prediction > 0
    
    any_test_positve_prediciton = infer_model_function(data, any_positive_model)
    any_test_positive_bools = any_test_positve_prediciton > 0
    

    cancer_risk = (biopsy_prediction + hinselman_prediction + schiller_prediction + citology_prediction)

    # Return a dictionary 
    output = {
        'biopsy_prediction': biopsy_bools,
        'hinselman_prediction': hinselman_bools,
        'schiller_prediction': schiller_bools,
        'citology_prediction': citology_bools,
        'any_test_positive': any_test_positive_bools,
        'cancer_risk': cancer_risk
    }

    return output

def infer_output_json(input_data:dict, infer_output_df=infer_output_df):
    input_data = {k.replace("_"," "): v for k, v in input_data.items()}
    print(input_data.items())
    df = pd.DataFrame([input_data])
    return infer_output_df(df)

if __name__ == '__main__':
    test_random_data = {
        "Age": 35, 
        "Number_of_sexual_partners": 2.0, 
        "First_sexual_intercourse": 18.0, 
        "Num_of_pregnancies": 4, 
        "Smokes": 1, 
        "Smokes_(years)": 15.0, 
        "Smokes_(packs/year)": 1,
        "Hormonal_Contraceptives": 1, 
        "Hormonal_Contraceptives (years)": 15.0, 
        "IUD": 0, 
        "IUD_(years)": 10.0,
        "STDs": 0,
        "STDs_(number)": 0,
        "STDs:condylomatosis": 0,
        "STDs:cervical_condylomatosis": 0, 
        "STDs:vaginal_condylomatosis": 0, 
        "STDs:vulvo-perineal_condylomatosis": 0, 
        "STDs:syphilis": 0,
        "STDs:pelvic_inflammatory_disease": 0, 
        "STDs:genital_herpes": 0,
        "STDs:molluscum_contagiosum": 0, 
        "STDs:AIDS": 0, 
        "STDs:HIV": 0, 
        "STDs:Hepatitis B": 0,
        "STDs:HPV": 0, 
        "STDs:_Number_of_diagnosis": 0, 
        "Dx:Cancer": 0, 
        "Dx:CIN": 0, 
        "Dx:HPV": 1, 
        "Dx": 0,
    }
    prediction = infer_output_json(test_random_data)
    print(prediction)
