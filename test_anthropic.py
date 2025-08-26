import streamlit as st
import requests
import os

# This test script reads the API key from the same secrets file.
# Make sure your .streamlit/secrets.toml file still exists and is correct.
try:
    API_KEY = st.secrets["ANTHROPIC_API_KEY"]
    print("✅ Successfully read API key from secrets.toml")
except Exception:
    print("❌ Error: Could not read API key from .streamlit/secrets.toml.")
    print("Please ensure the file exists at .streamlit/secrets.toml and is correctly formatted.")
    exit()

API_URL = "https://api.anthropic.com/v1/messages"
MODEL_NAME = "claude-3-sonnet-20240229"

headers = {
    "x-api-key": API_KEY,
    "content-type": "application/json",
    "anthropic-version": "2023-06-01"
}

data = {
    "model": MODEL_NAME,
    "max_tokens": 25,
    "messages": [{"role": "user", "content": "Hello, Claude"}]
}

print("--- Sending Request to Anthropic ---")
print(f"URL: {API_URL}")
print("------------------------------------")

try:
    response = requests.post(API_URL, headers=headers, json=data)
    # This line will cause an error if the status code is 4xx or 5xx
    response.raise_for_status() 
    
    print("\n✅ --- SUCCESS! --- ✅")
    print("Response from Anthropic:")
    print(response.json())
    print("--------------------")

except requests.RequestException as e:
    print(f"\n❌ --- FAILED! --- ❌")
    print(f"An error occurred: {e}")
    if e.response is not None:
        print(f"Status Code: {e.response.status_code}")
        print(f"Response Body: {e.response.text}")
    print("-------------------")