import requests

def handler(request):
    # Get deal status from query parameter
    status = request.args.get("status", "open")
    
    # Use your real token here
    api_token = "YOUR_PIPEDRIVE_TOKEN"
    company_domain = "YOUR_DOMAIN"  # e.g., pinkpineapple

    url = f"https://{company_domain}.pipedrive.com/api/v1/deals?status={status}&api_token={api_token}"
    response = requests.get(url)
    deals = response.json().get("data", [])

    return {
        "deals": [
            {
                "title": d["title"],
                "value": d["value"],
                "status": d["status"],
                "org_name": d.get("org_name"),
                "expected_close_date": d.get("expected_close_date")
            }
            for d in deals if d
        ]
    }
