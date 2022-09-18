aws-serverless-python-apigateway
==========

# Requiments
- [serverless](https://serverless.com/framework/)
- [python v3.8](https://www.python.org/downloads/)
- [pipenv](https://pipenv.readthedocs.io/en/latest/)

# Prepare the environment
To prepare the environment, you need to install the dependencies and run the following commands:
```sh-session
$ npm i
$ pipenv install
```

# Deployment
Serverless is used to create the AWS Lambda function, AWS Apigateway and DynamoDB table.

```sh-session
$ sls deploy 
```

# If problems occours during deploy
If you get this error: **ModuleNotFoundError: No module named 'distutils.cmd'**, try to fix installing:
```sh-session
sudo apt-get install python3.8-distutils
```
