import numexpr as ne
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def calculate_expression(expr: str) -> float:
    """Avalia expressões matemáticas simples de forma segura."""
    return float(ne.evaluate(expr))

if __name__ == "__main__":
    print("Server em execução...")
    mcp.run(transport="stdio")
