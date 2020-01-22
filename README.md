# Kaggle Deploy

This project has been started in order to serve the prediction endpoints that will provide the prediction for target input.
I'll be using models that I create for kaggle practice/competitions. The colab notebooks for each model will be attached alongside.

## Models

### nlp-getting-started
* Prediction endpoint: [https://kaggle-deploy.herokuapp.com/nlp-getting-started/predict](https://kaggle-deploy.herokuapp.com/nlp-getting-started/predict)
* Method: `POST`
* Body:
    * `text`: Array of string. Each string is a sentence.
    E.g.
```
{
    "text":["There's been an accident", "There be accident bruh!"]
}
```