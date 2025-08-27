from langchain.tools import Tool

def calculator_tool(expression):
    return eval(expression)

my_tool = Tool(
    name="Calculator",
    description="Computes arithmetic expressions",
    func=calculator_tool
)
print(my_tool.run("2 + 2 * 3"))  # Output: 8
