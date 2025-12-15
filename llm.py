import json
from prompt import FINAL_PROMPT
from output_schema import PlantReport
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

llm = OllamaLLM(
    model="llama3",
    temperature=0.3
)

prompt_template = PromptTemplate(
    template=FINAL_PROMPT,
    input_variables=["plant_name", "disease", "confidence"],
)


chain = prompt_template | llm | parser

def get_llm_report(plant_name, disease, confidence):
    try:
        raw = chain.invoke({
            "plant_name": plant_name,
            "disease": disease,
            "confidence": confidence
        })
        return PlantReport(**raw)
    except Exception as e:
        print("LLM parsing failed:", e)
        return None
