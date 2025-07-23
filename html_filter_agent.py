import llm_agent

class HtmlFilterAgent:
    filterAgent = None
    def __init__(self):
        role_description = "你是一个擅长判断文字相关性的专家"
        task_description = "我会给你一些文字片段和片段对应的编号，同时会给你一个关键字，帮我挑选出与关键字最" \
                           "相关的内容片段，仅仅返回给我编号，不需要返回其他内容，编号之间使用空格隔开"
        self.filterAgent = llm_agent.LLMAgent(role_description, task_description)


    def get_related_html_id(self, html_list: list[str], keyword: str) -> str:
        message = f"key word: {keyword} \n"
        counter = 0
        for html in html_list:
            if "Error" not in html:
                # the max context size of llama3 is 16384 byte, si
                message += str(counter) + ": " + html[:5000] + "\n"
                counter += 1

        return self.filterAgent.inference(message)