import json

def lambda_handler(event, context):

    # Get query params (API Gateway)
    params = event.get("queryStringParameters") or {}

    monthly_budget = float(params.get("budget", 1000))
    current_spend = float(params.get("spent", 850))

    usage_percent = (current_spend / monthly_budget) * 100

    if usage_percent >= 100:
        status = "exceeded"
        message = "You have exceeded your budget"
    elif usage_percent >= 80:
        status = "warning"
        message = "You have exceeded 80% of your budget"
    else:
        status = "ok"
        message = "Your spending is within budget"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": status,
            "budget": monthly_budget,
            "spent": current_spend,
            "usage_percent": round(usage_percent, 2),
            "message": message
        })
    }