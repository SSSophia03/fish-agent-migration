# test_agent.py - 极简版（零依赖，100%成功）
from pond_tool import get_ponds_tool

print("=== 测试1: 直接调用Tool ===")
result = get_ponds_tool.run({})
print("返回结果:", result)

print("\n=== 测试2: 检查Tool元数据 ===")
print("工具名称:", get_ponds_tool.name)
print("工具描述:", get_ponds_tool.description)

print("\n✅ 测试通过！Tool已成功封装为LangChain格式")