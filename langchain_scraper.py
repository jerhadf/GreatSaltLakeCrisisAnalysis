# import libraries
import os
os.environ["OPENAI_API_KEY"] = "your API here"
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import openpyxl
import pandas as pd
import numpy as np

# read in database with pandas
df = pd.read_excel('railwaypro v1.xlsx')
df.head();

# filter to company 
keyword = "Stadler"
filtered_std = df[df['Context'].str.contains(keyword)]
filtered_std.shape[0]
filtered_std.head()
filtered_std[['Title','Context']]

# use LangChain's DataFrameLoader to load filtered data into LangChain
from langchain.document_loaders import DataFrameLoader
loader = DataFrameLoader(filtered_std, page_content_column="Title")

# create LangChain QuestionAnswering chain - 
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

chain = load_qa_chain(llm=OpenAI(), chain_type="map_reduce")
query ="Give me the profile of Stadler, what they are supplying, who they're supplying to, where are they operate, etc."
chain.run(input_documents=loader.load(), question=query)