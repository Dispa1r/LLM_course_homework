# Agent homework 2

说是 Agent，其实作业内容主要是 RAG，这部分没什么难的的，说是 RAG，其实本质上居然是 multi agent，这里设计的很简单，
先提取关键词，然后用谷歌搜索获取相关内容，再提取搜索内容中相关的部分，配合维基百科一起喂进去


## 一些问题

作业要求的 llama3的能力其实很差，上下文就 16000个字节，导致我每个搜索内容最多只能使用 5000个token，其次，这个获取相关 html 的
agent 工作的也很差，感觉不如传统的向量数据库了，这里又去找了个 graph数据库存储搜索的内容，再进行相关度匹配