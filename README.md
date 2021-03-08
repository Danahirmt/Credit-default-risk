# Credit-default-risk

A quick view to develop a credit score to assess whether new customers will be good or bad payers.

Building docker image

```
make init
```


## Organization

├── Dockerfile
├── Makefile
├── README.md
├── environment.yml
├── notebooks
│   ├── EDA.ipynb <- Exploration
│   ├── Model.ipynb <- xgboost
└── src
    ├── clean.py
    ├── feature_engineering.py
    ├── read_data.py
    └── variables.py
