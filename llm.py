from llama_cpp import Llama

# Load the model onto GPU
llama3 = Llama(
    "./Meta-Llama-3.1-8B-Instruct-Q8_0.gguf",
    verbose=False,
    n_gpu_layers=-1,
    n_ctx=16384,    # This argument is how many tokens the model can take. The longer the better, but it will consume more memory. 16384 is a proper value for a GPU with 16GB VRAM.
)

def generate_response(_model: Llama, _messages: str) -> str:
    '''
    This function will inference the model with given messages.
    '''
    _output = _model.create_chat_completion(
        _messages,
        stop=["<|eot_id|>", "<|end_of_text|>"],
        max_tokens=512,    # This argument is how many tokens the model can generate.
        temperature=0,      # This argument is the randomness of the model. 0 means no randomness. You will get the same result with the same input every time. You can try to set it to different values.
        repeat_penalty=2.0,
    )["choices"][0]["message"]["content"]
    return _output