from langchain.tools import tool
import mysql.connector

@tool
def get_ponds_tool() -> list:
    """查询系统中所有池塘的ID和名称"""

    return [
        {"id": 1, "name": "池塘A"},
        {"id": 2, "name": "池塘B"},
        {"id": 3, "name": "池塘C"}
    ]
