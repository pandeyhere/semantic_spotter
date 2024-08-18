from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core import VectorStoreIndex
from IPython.display import HTML


import os
import openai
import pandas as pd

openai.api_key= os.getenv("OPENAI_API_KEY")
questions = ['What does the author say about AirbNb?', "I want to be a billionaire. What does Paul Graham say about that?",
             'What is the opinion of the author on India?']

def rag():
    try:
        reader = SimpleDirectoryReader(input_dir="data")
        documents = reader.load_data()
        print(f"Loaded {len(documents)} docs")

        # create parser and parse document into nodes
        parser = SimpleNodeParser.from_defaults()
        nodes = parser.get_nodes_from_documents(documents)

        # # build index
        index = VectorStoreIndex(nodes)

        # Construct Query Engine
        query_engine = index.as_query_engine()

        return query_engine

        # response = query_engine.query("What is Paul Graham's opinion on AirBNB?")

        # print(f"{response.response}")

        # print(f"{response.source_nodes}")

        # response.source_nodes[0].node.metadata['file_name']

        # response.source_nodes[1].score
    except Exception as e:
        print(e)
        raise Exception(f"Query Engine could not be constructed. {e.message}")

def query_response(user_input):
  try:
    query_engine = rag()
    response = query_engine.query(user_input)
    file_name = response.source_nodes[0].node.metadata['file_name']
    final_response = response.response + '\n Check further at ' + file_name + ' document'
    return final_response
  
  except Exception as e:
    print(e)
    raise Exception(f"Response could not be fetched. {e.message}")
  
def initialize_conv():
  try:
    print('Feel free to ask Questions regarding essays of Paul Graham. Press exit once you are done')
    while True:
        user_input = input()
        if user_input.lower() == 'exit':
            print('Exiting the program... bye')
            break
        else:
            response = query_response(user_input)
            data = HTML(f'<p style="font-size:20px">{response}</p>')
            with open("data.html", "w") as file:
                file.write(data.data)

  except Exception as e:
        print(e)
        raise Exception(f"RAG could not be queried. {e.message}")

if __name__ == "__main__":
    initialize_conv()