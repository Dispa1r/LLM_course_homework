import llm

class LLMAgent():
    def __init__(self, role_description: str, task_description: str, llm:str="bartowski/Meta-Llama-3.1-8B-Instruct-GGUF"):
        self.role_description = role_description   # Role means who this agent should act like. e.g. the history expert, the manager......
        self.task_description = task_description    # Task description instructs what task should this agent solve.
        self.llm = llm  # LLM indicates which LLM backend this agent is using.
    
    def inference(self, message:str) -> str:
        if self.llm == 'bartowski/Meta-Llama-3.1-8B-Instruct-GGUF': # If using the default one.
            # TODO: Design the system prompt and user prompt here.
            # Format the messsages first.
            messages = [
                {"role": "system", "content": f"{self.role_description}"},  # Hint: you may want the agents to speak Traditional Chinese only.
                {"role": "user", "content": f"{self.task_description}\n{message}"}, # Hint: you may want the agents to clearly distinguish the task descriptions and the user messages. A proper seperation text rather than a simple line break is recommended.
            ]
            return llm.generate_response(llm.llama3, messages)
        else:
            # TODO: If you want to use LLMs other than the given one, please implement the inference part on your own.
            return ""