import llm_agent

class KeyWordExtractAgent():
    keyWordAgent = None
    def __init__(self):
        role_description = "你是一个擅长从文字中提取关键词的专家"
        task_description = "我会给你一些文字片段，帮我从段文字中提取关键词，关键词数量在 3 个以内，返回给我这些关键词" \
                            "除此之外不需要返回其他数据，返回的关键词以相关度排序"
        self.keyWordAgent = llm_agent.LLMAgent(role_description, task_description)

    def extract_key_words(self, question) -> str:
        key_word_list_str =  self.keyWordAgent.inference(question)
        return key_word_list_str