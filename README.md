# andi-webservices
Webservice for the ANDI website

## Testing ANDI webservices
ANDI web-services is currently build on flask framework of python. This RESTful api takes two requests GET and POST implemented in script `callRFromWebService.py`. Internally this webservice is calling R script `functionforandi.R`.
The input to this REST call is a JSON object build using form input of the ANDI portal by filling in patient data. The output of this REST call is another JSON object that is used to display results as a line graph. The resulting JSON object consists of statistical calculations, computed from `functionforandi.R` script.

To test this webservice a REST client for chrome browser such as  [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop) can be used. 
At present the webservice runs at (http://145.100.58.103:9000/#/).

From within this client select `POST` from the dropdown list as a service. Enter the url (http://145.100.58.103:5000/formTestScores) in the field next to `POST`. Next, select the menu item `Body` and enter the following input example. After this click the `Send` button. 

### example input of this webservice
```javascript
{
  "0": {
    "id": "1111",
    "age": "2016-04-02T22:00:00.000Z",
    "dob": "2016-04-02T22:00:00.000Z",
    "dot": "2016-04-02T22:00:00.000Z",
    "sex": "0",
    "education": "3",
    "test": [
      {
        "id": "DART-raw_score",
        "label": "raw score",
        "Dataset": "DART",
        "SPSS name": "DARTRAW",
        "highborder": "100.001",
        "highweb": "100",
        "lowborder": "20",
        "lowweb": "0",
        "value": 55
      },
      {
        "id": "HADS-anxiety",
        "label": "Anxiety scale",
        "Dataset": "HADS",
        "SPSS name": "HADS_anxiety",
        "highborder": "9.001",
        "highweb": "21",
        "lowborder": "0",
        "lowweb": "0",
        "value": 12
      },
      {
        "id": "HADS-depression",
        "label": "Depression scale",
        "Dataset": "HADS",
        "SPSS name": "HADS_depression",
        "highborder": "9.001",
        "highweb": "21",
        "lowborder": "0",
        "lowweb": "0",
        "value": 12
      },
      {
        "id": "HADS-total",
        "label": "total score",
        "Dataset": "HADS",
        "SPSS name": "HADS_total",
        "highborder": "13.001",
        "highweb": "42",
        "lowborder": "0",
        "lowweb": "0",
        "value": 12
      }
    ]
  },
  "1": {
    "id": "2222",
    "age": "2016-04-02T22:00:00.000Z",
    "dob": "2016-04-02T22:00:00.000Z",
    "dot": "2016-04-02T22:00:00.000Z",
    "sex": "1",
    "education": "2",
    "test": [
      {
        "id": "DART-raw_score",
        "label": "raw score",
        "Dataset": "DART",
        "SPSS name": "DARTRAW",
        "highborder": "100.001",
        "highweb": "100",
        "lowborder": "20",
        "lowweb": "0",
        "value": 55
      },
      {
        "id": "HADS-anxiety",
        "label": "Anxiety scale",
        "Dataset": "HADS",
        "SPSS name": "HADS_anxiety",
        "highborder": "9.001",
        "highweb": "21",
        "lowborder": "0",
        "lowweb": "0",
        "value": 12
      },
      {
        "id": "HADS-depression",
        "label": "Depression scale",
        "Dataset": "HADS",
        "SPSS name": "HADS_depression",
        "highborder": "9.001",
        "highweb": "21",
        "lowborder": "0",
        "lowweb": "0",
        "value": 12
      },
      {
        "id": "HADS-total",
        "label": "total score",
        "Dataset": "HADS",
        "SPSS name": "HADS_total",
        "highborder": "13.001",
        "highweb": "42",
        "lowborder": "0",
        "lowweb": "0",
        "value": 12
      }
    ]
  },
  "conf": "99",
  "sig": "oneTailedRight",
  "nomative": "2016-01-14"
}
```


## If everything goes well the following example output of this webservice should be visible below in the `Postman` client.

```javascript
[
  {
    "id": 1111,
    "testname": "DART-raw_score",
    "longtestname": "Dutch Adult Reading Test raw score ",
    "plotname": "DART raw score",
    "shortestname": "DART raw score",
    "tails": "oneTailedRight",
    "inneredge": -99999,
    "outeredge": 2.3281,
    "univariatedifferences": -0.8176,
    "univariateT": -0.94,
    "univariatedf": 2170,
    "univariatep": "0.174",
    "multivariatedifference": -8.433,
    "multivariateT": -2.0892,
    "multivariatedf": "4, 59",
    "multivariatep": "1.000"
  },
  {
    "id": 1111,
    "testname": "HADS-anxiety",
    "longtestname": "Hospital Anxiety Depression Scale Anxiety scale ",
    "plotname": "HADS Anxiety scale",
    "shortestname": "HADS anxiety",
    "tails": "oneTailedRight",
    "inneredge": -99999,
    "outeredge": 2.386,
    "univariatedifferences": -2.8564,
    "univariateT": -2.68,
    "univariatedf": 64,
    "univariatep": "0.005",
    "multivariatedifference": -8.433,
    "multivariateT": -2.0892,
    "multivariatedf": "4, 59",
    "multivariatep": "1.000"
  },
  {
    "id": 1111,
    "testname": "HADS-depression",
    "longtestname": "Hospital Anxiety Depression Scale Depression scale ",
    "plotname": "HADS Depression scale",
    "shortestname": "HADS depression",
    "tails": "oneTailedRight",
    "inneredge": -99999,
    "outeredge": 2.3833,
    "univariatedifferences": -2.872,
    "univariateT": -2.77,
    "univariatedf": 67,
    "univariatep": "0.004",
    "multivariatedifference": -8.433,
    "multivariateT": -2.0892,
    "multivariatedf": "4, 59",
    "multivariatep": "1.000"
  },
  {
    "id": 1111,
    "testname": "HADS-total",
    "longtestname": "Hospital Anxiety Depression Scale total score ",
    "plotname": "HADS total score",
    "shortestname": "HADS total",
    "tails": "oneTailedRight",
    "inneredge": -99999,
    "outeredge": 2.388,
    "univariatedifferences": -1.887,
    "univariateT": -1.76,
    "univariatedf": 62,
    "univariatep": "0.042",
    "multivariatedifference": -8.433,
    "multivariateT": -2.0892,
    "multivariatedf": "4, 59",
    "multivariatep": "1.000"
  },
  {
    "id": 2222,
    "testname": "DART-raw_score",
    "longtestname": "Dutch Adult Reading Test raw score ",
    "plotname": "DART raw score",
    "shortestname": "DART raw score",
    "tails": "oneTailedRight",
    "inneredge": -99999,
    "outeredge": 2.3281,
    "univariatedifferences": -0.4726,
    "univariateT": -0.54,
    "univariatedf": 2170,
    "univariatep": "0.294",
    "multivariatedifference": -7.999,
    "multivariateT": -1.8684,
    "multivariatedf": "4, 59",
    "multivariatep": "1.000"
  },
  {
    "id": 2222,
    "testname": "HADS-anxiety",
    "longtestname": "Hospital Anxiety Depression Scale Anxiety scale ",
    "plotname": "HADS Anxiety scale",
    "shortestname": "HADS anxiety",
    "tails": "oneTailedRight",
    "inneredge": -99999,
    "outeredge": 2.386,
    "univariatedifferences": -2.8084,
    "univariateT": -2.64,
    "univariatedf": 64,
    "univariatep": "0.005",
    "multivariatedifference": -7.999,
    "multivariateT": -1.8684,
    "multivariatedf": "4, 59",
    "multivariatep": "1.000"
  },
  {
    "id": 2222,
    "testname": "HADS-depression",
    "longtestname": "Hospital Anxiety Depression Scale Depression scale ",
    "plotname": "HADS Depression scale",
    "shortestname": "HADS depression",
    "tails": "oneTailedRight",
    "inneredge": -99999,
    "outeredge": 2.3833,
    "univariatedifferences": -2.872,
    "univariateT": -2.77,
    "univariatedf": 67,
    "univariatep": "0.004",
    "multivariatedifference": -7.999,
    "multivariateT": -1.8684,
    "multivariatedf": "4, 59",
    "multivariatep": "1.000"
  },
  {
    "id": 2222,
    "testname": "HADS-total",
    "longtestname": "Hospital Anxiety Depression Scale total score ",
    "plotname": "HADS total score",
    "shortestname": "HADS total",
    "tails": "oneTailedRight",
    "inneredge": -99999,
    "outeredge": 2.388,
    "univariatedifferences": -1.846,
    "univariateT": -1.72,
    "univariatedf": 62,
    "univariatep": "0.045",
    "multivariatedifference": -7.999,
    "multivariateT": -1.8684,
    "multivariatedf": "4, 59",
    "multivariatep": "1.000"
  }
] 
```



## Running with Docker
* Images are automatically build on docker hub
* To get Docker image from docker hub:
`docker pull andinl/andi-webservices`
* To run the container and bind to port 5000 run: `docker run -d -p 5000:5000 andi-nl/andi-webservices`
