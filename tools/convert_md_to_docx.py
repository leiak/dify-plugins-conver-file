from collections.abc import Generator
from typing import Any
import markdown
from htmldocx import HtmlToDocx
from io import BytesIO
from docx import Document

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class ConvertMdToDocxTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        content = tool_parameters.get("content", "")
        filename = tool_parameters.get("filename", "output")
        
        if not content:
            raise Exception("Content cannot be empty.")

        # 将 Markdown 转换为 HTML
        html_content = markdown.markdown(content)
        
        # 将 HTML 转换为 DOCX
        # htmldocx 需要一个 Document 对象
        document = Document()
        new_parser = HtmlToDocx()
        
        # 解析 HTML 并添加到文档
        new_parser.add_html_to_document(html_content, document)
        
        # 保存到缓冲区
        docx_buffer = BytesIO()
        document.save(docx_buffer)
        docx_bytes = docx_buffer.getvalue()
        
        # 将 DOCX 作为 blob 消息返回
        yield self.create_blob_message(
            blob=docx_bytes, 
            meta={'mime_type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'filename': f"{filename}.docx"}
        )
