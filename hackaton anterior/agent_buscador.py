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
    agent_id = credentials["agent_buscador"]

# prompt template con una variables
prompt = PromptTemplate(
    input_variables=["name", "question"],
    template="Hola, mi nombre es {name} y tengo la siguiente pregunta: {question}",
)

userInput = input("Ingrese su pregunta: ")

# Judini
url = "https://playground.judini.ai/api/v1/agent/" + agent_id
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + api_key,
}
data = {
    "messages": [
        {"role": "user", "content": prompt.format(name="Alfonso", question=userInput)}
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

print(tokens)

titles = re.findall(r"\[(.*?)\]", tokens)
unique_titles = list(set(titles))

if unique_titles == [""]:
    titles = list(unique_titles)
else:
    # Si no se encuentran corchetes, seleccionar el texto después de "son:"
    pattern = r"son:\s*-\s*(.*?)\s*-"
    matches = re.findall(pattern, tokens)
    titles = list(matches)

for title in unique_titles:
    print(title)

output = {"titles": unique_titles}

with open("judini/titles.json", "w") as file:
    json.dump(output, file)
