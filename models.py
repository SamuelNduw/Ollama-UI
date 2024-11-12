import requests

def get_local_models():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        response.raise_for_status()  # Raises an error for bad status codes
        data = response.json()  # Parse JSON directly from the response

        # Extract all model names
        model_names = [model['name'] for model in data.get('models', [])]
        return model_names  # Return the list of model names
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"
    

