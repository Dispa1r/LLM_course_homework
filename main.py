import html_filter_agent
import key_word_extract_agent
import llm
import search_tool
import asyncio

if __name__ == '__main__':
    test_question = '請問誰是TaylorSwift？'

    keyWordAgent = key_word_extract_agent.KeyWordExtractAgent()
    keyWordList = keyWordAgent.extract_key_words(test_question)

    htmlFilterAgent = html_filter_agent.HtmlFilterAgent()
    answers = asyncio.run(search_tool.search(test_question))
    htmlIdList = htmlFilterAgent.get_related_html_id(answers, keyWordList).split(" ")

    user_prompt = ""
    for id in htmlIdList:
        user_prompt += answers[int(id)][:5000]
        user_prompt += "\n"

    wikipediaAnswer = search_tool.search_by_wikipedia(keyWordList)
    user_prompt += "这里是维基百科的一些介绍："
    user_prompt += wikipediaAnswer[:5000]

    messages = [
        {"role": "system", "content": "你是 LLaMA-3.1-8B，是用來回答問題的 AI。使用中文時只會使用繁體中文來回問題。"},
        # System prompt
        {"role": "user", "content": "这里是网上现有的一些资料" + user_prompt + "\n 下面是问题" + test_question},  # User prompt
    ]

    print(llm.generate_response(llm.llama3, messages))