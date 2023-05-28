%pip install --upgrade pip
%pip install openai
%pip install langchain

api_key = '############'
from langchain.llms import OpenAI
from langchain import PromptTemplate

template ="""
You are a good at mathematics.
You will be given a mathematical statement and you have to correct it.

Example - 

Input: "There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $40"
Corrected - 
"There are 5 items on the menu and each cost $10 on average. Even if we get all of them, We will have to pay $50"

Input: "I have 3 apples, and each costs $2. If I buy 4 more, I'll have 16 apples in total."
Corrected -
"I have 3 apples, and each costs $2. If I buy 4 more, I'll have 7 apples in total."

Input: "A recipe calls for 2 cups of flour, and I want to make 4 times the recipe. I need 6 cups of flour."
Corrected -
"A recipe calls for 2 cups of flour, and I want to make 4 times the recipe. I need 8 cups of flour."

Input: {question}
Corrected -
"""


prompt_template = PromptTemplate(
    input_variables=["question"],
    template=template
)

# print(prompt_template.format(question=" The best technologies after 2015, include all."))
questions = [
    "I bought a shirt that was on sale for 20% off its original price of $50. I saved $2!",
    "A recipe calls for 2 cups of flour, and I want to make 4 times the recipe. I need 6 cups of flour.",
    "There are 20 students in a class, and each student has 10 pencils. In total, there are 100 pencils.",
]

llm = OpenAI(temperature=0)
answer = []
for question in questions:
    prompt = prompt_template.format(question=question)
    res = llm(prompt)
    answer.append(res)

for i in range(len(questions)):
    print("Question: ", questions[i])
    print("Corrected: \n", answer[i])
    print()
