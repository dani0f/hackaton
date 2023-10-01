from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os
import requests
import json
from judini.agent import Agent
import re

"""
 Prompt Template con Judini
"""

with open("judini/credentials.json") as f:
    credentials = json.load(f)
    api_key = credentials["judini"]
    agent_id = credentials["agent_programador"]

with open("judini/presentacion.json", "r") as file:
    data = json.load(file)
    presentacion = data["token"]

# prompt template con una variables
prompt = PromptTemplate(
    input_variables=["name", "presentacion"],
    template="Hola, mi nombre es {name} y tengo la siguiente idea de presentacion: {presentacion}",
)

# Judini
url = "https://playground.judini.ai/api/v1/agent/" + agent_id
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + api_key,
}
data = {
    "messages": [
        {
            "role": "user",
            "content": prompt.format(name="Alfonso", presentacion=presentacion),
        }
    ]
}
# print(data)
response = requests.post(url, headers=headers, json=data, stream=True)
raw_data = ""
tokens = ""
for chunk in response.iter_content(chunk_size=1024):
    if chunk:
        raw_data = chunk.decode("utf-8").replace("data: ", "")
        if raw_data != "":
            lines = raw_data.strip().splitlines()
            for line in lines:
                print(line)
                line = line.strip()
                if line and line != "[DONE]":
                    try:
                        json_object = json.loads(line)
                        print("json_ok")
                        result = json_object["data"]
                        result = result.replace("\n", "")
                        tokens += result
                    except json.JSONDecodeError:
                        print(
                            f"Error al decodificar el objeto JSON en la línea: {line}"
                        )

# Parse the data string into a Python object
data = json.loads(tokens)

# Write the data to a JSON file
with open("judini/presentacion.json", "w") as file:
    json.dump(data, file)
