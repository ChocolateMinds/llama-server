from flask import Flask, request, jsonify
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from dotenv import load_dotenv
import os

# Load environment variables

load_dotenv()

MODEL = os.getenv("MODEL")
TEMPERATURE = os.getenv("TEMPERATURE")
MAX_TOKENS = os.getenv("MAX_TOKENS")
TOP_P = os.getenv("TOP_P")

app = Flask(__name__)

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

def load_llm():
    
    llm:LlamaCpp  = LlamaCpp(
        model_path=MODEL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        callback_manager=callback_manager, 
        verbose=True,
    )
    return llm

model = load_llm()
