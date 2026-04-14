# aws-budget-monitor-api
# AWS Budget Monitoring API

A simple serverless API built using AWS Lambda and API Gateway that simulates budget tracking logic.

---

## Architecture
API Gateway → AWS Lambda → JSON Response

---

## Features
- Accepts budget and spending values via query parameters
- Calculates usage percentage
- Returns status: OK / WARNING / EXCEEDED
- Fully serverless deployment

---

## Endpoint
