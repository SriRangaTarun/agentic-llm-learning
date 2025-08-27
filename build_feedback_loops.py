def quality_checker(response):
    if "error" in response.lower():
        return "Retry"
    return "Accept"

response = "The result is ERROR."
if quality_checker(response) == "Retry":
    print("Output failed check, will retry subtask.")
