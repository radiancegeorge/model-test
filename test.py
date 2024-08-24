from llama_cpp import Llama
import json
llm = Llama(
      model_path="model/llama-2-7b-chat.Q4_K_M.gguf",
      n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)

def call_chat_completion (role="user", question=""):
    output = llm.create_chat_completion(
            messages = [
                {
                    "role": role,
                    "content": question
                }
            ],
            max_tokens=5
            
    )
    return json.dumps(output)
