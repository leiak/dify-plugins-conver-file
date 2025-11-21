from collections.abc import Generator
from typing import Any
import markdown
from xhtml2pdf import pisa
from io import BytesIO

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class ConvertMdToPdfTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        content = tool_parameters.get("content", "")
        filename = tool_parameters.get("filename", "output")
        
        if not content:
            raise Exception("Content cannot be empty.")

        # 将 Markdown 转换为 HTML
        html_content = markdown.markdown(content)
        
        # 将 HTML 转换为 PDF
        pdf_buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html_content, dest=pdf_buffer)
        
        if pisa_status.err:
            raise Exception("PDF generation failed.")
            
        pdf_bytes = pdf_buffer.getvalue()
        
        # Return the PDF as a blob message
        yield self.create_blob_message(
            blob=pdf_bytes, 
            meta={'mime_type': 'application/pdf', 'filename': f"{filename}.pdf"}
        )
