# Cervical Cancer Risk Classification ![EDA](https://img.icons8.com/ios/30/000000/search.png)

## Challenge ![Interpret](https://img.icons8.com/ios/30/000000/presentation.png)

- Part 1: EDA 
    Extract the data from the csv file and use some techniques to gain insights. 

- Part 2: ETL 
    Clean the data and prepare it to be loaded in the next step.

- Part 3: Modeling
    Create some Machine Learning models to predict the classification, choose the best model in your opinion, justify your election and make it as prepared as you can to be ready for deployment.

- Part 4: Interpret
    Explain your results using metrics and visualizations techniques and write a short post in which you try to explain the project and your work to a non-technical audience.

## Solution ![Modeling](https://img.icons8.com/ios/30/000000/brain.png)

- Part 1-3.1: EDA, ETL and Modelling: Find the solution in the notebook `cervical_cancer.ipynb`
- Part 3.2: Model: The best model(s) from the notebook is saved in `model.py`
- Part 3.2: Deployment: Deployment with FAST API - Find the solution in `api.py`. The model is saved in `model.py`
- Part 4: The report is in `REPORT.md` file.

### Run the API ![API](https://img.icons8.com/ios/30/000000/api.png)

1. Install the requirements: `pip install -r requirements.txt` 
2. Run the API: `uvicorn api:app --reload` or to debug `uvicorn api:app --log-level debug `
3. Run the test: `python api_test.py` (there is a bug with the dataset labels and the api data validation, a replacement is needed " " for "_" in the models feature keys) 

## Contenerization ![Docker](https://img.icons8.com/ios/30/000000/docker.png)

1. Build the image: `docker build -t model .` 
2. Run the container: `docker run -d --name model -p 80:80 model`
