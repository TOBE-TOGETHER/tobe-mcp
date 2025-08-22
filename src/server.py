"""Main MCP server implementation for TOBE MCP."""

from pathlib import Path
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

from src.prompts.developer import developer_prompt
from src.prompts.ui_designer import ui_designer_prompt
from src.prompts.english_teacher import english_teacher_prompt
from src.prompts.article_writer import article_writer_prompt

def main():
    """Main entry point for the MCP server."""
    tobe_mcp = FastMCP()
    developer_prompt(tobe_mcp)
    ui_designer_prompt(tobe_mcp)
    english_teacher_prompt(tobe_mcp)
    article_writer_prompt(tobe_mcp)
    tobe_mcp.run()


if __name__ == "__main__":
    main()