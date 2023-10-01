import os
import requests
import json
from judini.agent import Agent
from langchain.prompts import PromptTemplate

"""
Prompt Template con Judini
"""

with open("judini/credentials.json") as f:
    credentials = json.load(f)
    api_key = credentials["judini"]
    agent_id = credentials["agent_resumidor"]

# Read titles from "titles.json" file
with open("judini/titles.json", "r") as file:
    data = json.load(file)
    titles = data["titles"]

# Create prompts using the titles
prompts = []
for title in titles:
    prompt = PromptTemplate(
        input_variables=["name"],
        template=f"Hola, mi nombre es {{name}} y los textos a resumir son: {title}",
    )
    prompts.append(prompt.format(name="Alfonso"))

# Judini
url = "https://playground.judini.ai/api/v1/agent/" + agent_id
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + api_key,
}

tokens = ""
for prompt in prompts:
    data = {"messages": [{"role": "user", "content": prompt}]}
    response = requests.post(url, headers=headers, json=data, stream=True)
    raw_data = ""
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            raw_data = chunk.decode("utf-8").replace("data: ", "")
            if raw_data != "":
                lines = raw_data.strip().splitlines()
                for line in lines:
                    line = line.strip()
                    if line and line != "[DONE]":
                        try:
                            json_object = json.loads(line)
                            result = json_object["data"]
                            result = result.replace("\n", "")
                            tokens += result
                        except json.JSONDecodeError:
                            print(
                                f"Error al decodificar el objeto JSON en la línea: {line}"
                            )

output = {"token": tokens}

with open("judini/presentacion.json", "w") as file:
    json.dump(output, file)
