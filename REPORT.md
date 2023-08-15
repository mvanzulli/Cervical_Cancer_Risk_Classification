### Cervical Cancer Risk Detection Report

Cervical cancer is a significant health concern for women worldwide [ [2](),[3]() ]. In 2023, an estimated 13,960 women in the United States will be diagnosed with invasive cervical cancer [6]. Early detection of cervical cancer is crucial for effective prevention and treatment. 

This report analyzes various factors and their correlation with the risk of cervical cancer based on a dataset from the [UCI Machine Learning Repository](https://archive-beta.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29#). However, the dataset used in the analysis has some limitations. There were missing values in certain variables, which were removed from the analysis. Additionally, there was an imbalance in positive and negative cases for each cervical cancer test, which could potentially bias the model's predictions.

The analysis reveals that the age of sexual activity onset and the number of sexual partners are relevant factors in determining the risk of cervical cancer. Women who began being sexually active between the ages of 15 and 20 appear to have a higher risk. A greater number of sexual partners could also increase the risk, as cervical cancer is often linked to sexually transmitted diseases. A similar behaviour is reported in the literature [5]()

The study also indicates a correlation between Human Papillomavirus (HPV) and cervical cancer. Furthermore, a positive exam for cervical cancer is correlated with other sexually transmitted diseases such as condylomatosis, HIV, and Vulvo Pernial Condylomatosis [2](). However, preventive methods such as the use of hormonal contraceptives and intrauterine devices (IUD) also show a potential correlation with cervical cancer risk [3](). One of this work findings is that: womans who have used oral contraceptives for 5 or more years have a higher risk compared to those who have never used them. Smoking, on the other hand, does not show a significant impact on the risk of cervical cancer in this dataset [4]().

To develop a tool capable of predicting cervical cancer risk, machine learning models were implemented form the literature [1](). Several models with different complexities, including Logistic Regression, Random Forest, AdaBoost, and XGBoost, were trained and evaluated based on precision and recall. Precision measures how well the model predicts cancer risk overall, while recall measures how well the model identifies positive cases, paying more attention to false positives. A comparison analysis between one single model to estiamte the risk or a combination of models is presented.

In summary, the models provide valuable predictive ability for cervical cancer risk based on several variables. And it is demonstrated that for this case multiple models can be combined to improve the overall performance. However, the dataset used in this analysis has some limitations, and further multidisciplinary research is needed to develop a more robust model.


### References

- 1:  [Cervical cancer diagnosis model using extreme gradient boosting and bioinspired firefly optimization](https://www.hindawi.com/journals/sp/2021/5540024/) Khan, I. U., Aslam, N., Alshehri, R., Alzahrani, S., Alghamdi, M., Almalki, A., & Balabeed, M. (2021). Cervical cancer diagnosis model using extreme gradient boosting and bioinspired firefly optimization. Scientific programming, 2021, 1-10.

- 2: [Risk factors for and prevention of human papillomaviruses (HPV), genital warts and cervical cancer.](https://www.sciencedirect.com/science/article/pii/S0163445312003106?casa_token=pv_KNCxntkwAAAAA:tcNXVL6Jl4J4Wbts93d4zQ4If_pUloTGa4mzLMQ8wJ3Fn_3LV8A0PwHYtwY9vlO38TZ8D-LHwQ): Chelimo, C., Wouldes, T. A., Cameron, L. D., & Elwood, J. M. (2013). Risk factors for and prevention of human papillomaviruses (HPV), genital warts and cervical cancer. Journal of Infection, 66(3), 207-217.

- 3: [Cervical cancer and use of hormonal contraceptives: a systematic review](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(03)12949-2/fulltext): Smith, J. S., Green, J., de Gonzalez, A. B., Appleby, P., Peto, J., Plummer, M., ... & Beral, V. (2003). Cervical cancer and use of hormonal contraceptives: a systematic review. The Lancet, 361(9364), 1159-1167.

- 4: [Smoking and cervical cancer—current status: a review](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=8ccdce22f030c7361465cf09d0cf6e71103f0dd5) Winkelstein Jr, W. (1990). Smoking and cervical cancer—current status: a review. American Journal of Epidemiology, 131(6), 945-957.

- 5: [Risk factors for human papillomavirus exposure and co-factors for cervical cancer in Latin America and the Caribbean.](https://www.sciencedirect.com/science/article/abs/pii/S0264410X08007238?casa_token=UUAAsyeuWekAAAAA:SOnEpY7F8YznTDLYBgicadh0kZMWHZaFuziMU-1yiV5m5o-h49f8dLLWvB-3rXQdWOMd8LBfsA) Almonte, M., Albero, G., Molano, M., Carcamo, C., García, P. J., & Pérez, G. (2008). Risk factors for human papillomavirus exposure and co-factors for cervical cancer in Latin America and the Caribbean. Vaccine, 26, L16-L36.

- 6:[Cervical Cancer: Statistics 2023](https://www.cancer.net/cancer-types/cervical-cancer/statistics#:~:text=How%20many%20people%20are%20diagnosed,with%20cervical%20cancer%20in%202020.): https://www.cancer.net/cancer-types/cervical-cancer/statistics#:~:text=How%20many%20people%20are%20diagnosed,with%20cervical%20cancer%20in%202020.
