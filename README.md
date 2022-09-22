## XGBoost Rosmann Sales Predictor 
 

**Request URL**:  [https://rosmann-forecast-ijfnrlfmcq-uk.a.run.app/predict](https://rosmann-forecast-ijfnrlfmcq-uk.a.run.app/predict)

**Request Type**: POST


**Example Input Payload  for XGBoost Rosmann Sales Predictor:** 
    
    {
        "Store": 1234,
        "DayOfWeek": 4,
        "Date": "2013-02-07",
        "Customers": 1,
        "Open": 1,
        "Promo": 0,
        "StateHoliday": "b",
        "SchoolHoliday": 0
    }


| Key           | Description                                                                                                                                                          | Data Type  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Store         | A unique Id for each store.                                                                                                                                          | Integer    |
| DayOfWeek     | Numerical indicator for the day of the week.                                                                                                                         | Integer    |
| Date          | Date of turnover or sale.                                                                                                                                            | String     |
| Customers     | The number of customers on a given day.                                                                                                                              | Integer    |
| Open          | An indicator for whether the store was open.                                                                                                                         | Integer    |
| Promo         | Indicates whether a store is running a promo on that day.                                                                                                            | Integer    |
| StateHoliday  | Indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. | String     |
| SchoolHoliday | Indicates if the (Store, Date) was affected by the closure of public schools                                                                                         | Integer    |



**Example Output Response  for XGBoost Rosmann Sales Predictor:** 
    
    {"Sales": 285.78}


| Key   | Description                                                       | Data Type |
|-------|-------------------------------------------------------------------|-----------|
| Sales | The turnover for any given day (this is what you are predicting). | Float     |

