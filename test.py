from llama_cpp import Llama
import json

def call_chat_completion (role="user", question=""):
    llm = Llama(
        model_path="model/llama-2-7b-chat.Q4_K_M.gguf",
        n_gpu_layers=-1, # Uncomment to use GPU acceleration
        # seed=1337, # Uncomment to set a specific seed
        # n_batch=32,
        n_ctx=2048, # Uncomment to increase the context window
        split_mode=2
)

    output = llm.create_chat_completion(
            messages = [
                {
                    "role": role,
                    "content": question
                }
            ],
            # max_tokens=5
            # stop=["."],
            
            
    )
    return json.dumps(output)
