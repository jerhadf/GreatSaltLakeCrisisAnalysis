import openai
import os
import configparser
import langchain as lc  # Import LangChain
from langchain import PromptTemplate, LLMChain, OpenAI
from langchain.memory import ConversationBufferMemory

# config API keys
config = configparser.ConfigParser()
config.read('config.ini')
openai_key = config['openai']['key']
openai.api_key = openai_key

# Read stakeholder groups from file
with open('data/stakeholders.txt', 'r') as f:
    stakeholder_groups = [line.strip() for line in f]

# Read questions from file
with open('data/GSL_questions.txt', 'r') as f:
    questions = [line.strip() for line in f]

# Create a prompt component using a template
template = """
You are a representative of the stakeholder group {stakeholder} in Utah, speaking from your own point of view. 
From your own first-person perspective, answer the following question about the Great Salt Lake drying crisis: 
Please provide an insightful, concrete, detailed, personal, relevant, and opinionated response. 
Imagine you are contributing to an environmental stakeholder survey, with the history of the conversation below. 
{chat_history}
Interviewer: {question}
You:"""

# prompt = PromptTemplate(
#     input_variables=["stakeholder", "question", "chat_history"],
#     template=template
# )

# For each stakeholder group, generate a response
for stakeholder in stakeholder_groups[0:5]:
    filename = f"responses/{stakeholder.replace(' ', '_')}_response.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # Create a chain component using the model, prompt and memory
    llm_chain = LLMChain(
        llm=OpenAI(temperature=0.5, openai_api_key=openai_key, max_tokens=500), 
        prompt=PromptTemplate.from_template(template),
        verbose=True,
        # Create a memory component for this conversation
        memory=ConversationBufferMemory(memory_key="chat_history", 
                                        input_key="input",
                                        output_key='output', 
                                        return_messages=True),
    )
    # loop through the questions and generate a response for each 
    for question in questions[0:3]:
        print(f"Generating response for {stakeholder} to question: {question}")
        # Get the output from the chain - with a limit of ~5 sentences (300 tokens)
        response = llm_chain.predict(
            # Set the input for the chain (the stakeholder and the question)
            stakeholder=stakeholder, 
            question=question,
            chat_history=llm_chain.memory.load_memory_variables({})
        )
        
        # Add the response to the memory as context 
        llm_chain.memory.save_context({"question": question, "response": response})

        # Open the file in append mode and write the question as a comment and then the response
        with open(filename, "a") as file:
            file.write("# " + question + "\n" + response.strip() + "\n\n")