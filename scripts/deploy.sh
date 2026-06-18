#!/bin/bash

# Deploy script for AWS Lambda

zip -r deployment.zip src/

aws lambda create-function --function-name transaction-service \
    --zip-file fileb://deployment.zip \
    --handler main.app \
    --runtime python3.12 \
    --role arn:aws:iam::123456789012:role/lambda-execution-role