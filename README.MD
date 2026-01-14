# 渔业系统Agent化改造实验

**目标**：将传统Python后端服务封装为LangChain Tool，探索自动化系统向LLM智能体架构演进的路径。

## 项目结构

## 技术栈
- **核心框架**：LangChain 0.1.13 (`@tool` 装饰器)
- **语言模型**：DeepSeek API (`deepseek-chat`)
- **数据库**：MySQL（当前使用模拟数据确保可运行性）
- **编程语言**：Python 3.10

## 文件说明
- `original_code.py`: 从原项目复制的真实函数（保留原始风格）
- `pond_tool.py`: 添加@tool装饰器后的版本
- `test_agent.py`: 验证LLM能否自动调用该工具

## 运行步骤
1. 通过模拟的数据来实现验证
2. `pip install -r requirements.txt`
3. `set OPENAI_API_KEY="sk-你的DeepSeek密钥"`
4. `python test_agent.py`

## 预期输出
=== 测试1: 直接调用Tool ===
返回结果: [{'id': 1, 'name': '池塘A'}, {'id': 2, 'name': '池塘B'}, {'id': 3, 'name': '池塘C'}]

=== 测试2: 检查Tool元数据 ===
工具名称: get_ponds_tool

工具描述: get_ponds_tool() -> list - 查询系统中所有池塘的ID和名称
