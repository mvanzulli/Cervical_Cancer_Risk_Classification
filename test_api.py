import requests
import json

# Define the URL of your API
url = "http://127.0.0.1:8000/predict/"

# Define the data you want to send to the API
data = {
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
        "STDs (number)": 0,
        "STDs:condylomatosis": 0,
        "STDs:cervical condylomatosis": 0, 
        "STDs:vaginal condylomatosis": 0, 
        "STDs:vulvo-perineal condylomatosis": 0, 
        "STDs:syphilis": 0,
        "STDs:pelvic inflammatory disease": 0, 
        "STDs:genital herpes": 0,
        "STDs:molluscum contagiosum": 0, 
        "STDs:AIDS": 0, 
        "STDs:HIV": 0, 
        "STDs:Hepatitis B": 0,
        "STDs:HPV": 0, 
        "STDs: Number of diagnosis": 0, 
        "Dx:Cancer": 0, 
        "Dx:CIN": 0, 
        "Dx:HPV": 1, 
        "Dx": 0,
    }
# Make the POST request to your API
response = requests.post(url, json=data)

# Print out the response
print(response.status_code)
print(response.json())

print(response.text)
