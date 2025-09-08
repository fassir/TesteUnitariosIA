from langchain.prompts import PromptTemplate
from langchain import LLMChain
from langchain.llms import AzureChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools.python.tool import PythonREPLTool

function_code = """
import numpy as np

def integral_polinomial(coef, a, b):
    '''
    Calcula a integral definida de um polinômio entre os limites a e b.
    coef: lista de coeficientes, do termo de maior grau ao menor.
    a, b: limites de integração.
    '''
    p = np.poly1d(coef)
    integral = p.integ()
    return integral(b) - integral(a)
"""

prompt = PromptTemplate(
    input_variables=["code"],
    template="""Você é um especialista em Python. Gere testes unitários usando pytest para a função abaixo, cobrindo casos típicos e limites matemáticos:

{code}

Retorne apenas o código dos testes.
"""
)

llm = AzureChatOpenAI(deployment_name="SeuDeployment", temperature=0)

chain = LLMChain(llm=llm, prompt=prompt)
generated_tests = chain.run(function_code)

tools = [
    Tool(
        name="PythonExecutor",
        func=PythonREPLTool().run,
        description="Executa código Python para validar testes unitários"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

result = agent.run(f"{function_code}\n{generated_tests}\nExecute os testes e informe o resultado.")

print("Testes Gerados:\n", generated_tests)
print("Resultado da Execução:\n", result)
