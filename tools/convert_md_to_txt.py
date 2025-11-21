from collections.abc import Generator
from typing import Any
import markdown
from bs4 import BeautifulSoup

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class ConvertMdToTxtTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        content = tool_parameters.get("content", "")
        filename = tool_parameters.get("filename", "output")
        
        if not content:
            raise Exception("Content cannot be empty.")

        # 将 Markdown 转换为 HTML
        html_content = markdown.markdown(content)
        
        # 使用 BeautifulSoup 从 HTML 中提取文本
        soup = BeautifulSoup(html_content, "html.parser")
        text_content = soup.get_text(separator='\n\n')
        
        # Create bytes
        txt_bytes = text_content.encode('utf-8')
        
        # Return the TXT as a blob message
        yield self.create_blob_message(
            blob=txt_bytes, 
            meta={'mime_type': 'text/plain', 'filename': f"{filename}.txt"}
        )
