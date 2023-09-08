from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from dotenv import load_dotenv
import os

# Load env 
load_dotenv()
MODEL = os.getenv("MODEL")
TEMPERATURE = os.getenv("TEMPERATURE")
MAX_TOKENS = os.getenv("MAX_TOKENS")
TOP_P = os.getenv("TOP_P")

def load_llm():

# Make sure the model path is correct for your system!
# Callbacks support token-wise streaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

    llm:LlamaCpp  = LlamaCpp(
        model_path=MODEL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=TOP_P,
        callback_manager=callback_manager, 
        verbose=True, # Verbose is required to pass to the callback manager
    )

    return llm

model = load_llm()

prompt = """
    Question: What is BTC?
    """

answer:str = model(prompt)

print(answer)