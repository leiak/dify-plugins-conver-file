from collections.abc import Generator
from typing import Any
import markdown

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class ConvertMdToHtmlTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        content = tool_parameters.get("content", "")
        filename = tool_parameters.get("filename", "output")
        
        if not content:
            raise Exception("Content cannot be empty.")

        # 将 Markdown 转换为 HTML
        # 启用扩展以获得更好的渲染（表格、代码块等）
        html_body = markdown.markdown(content, extensions=['extra', 'codehilite', 'toc'])
        
        # 定义现代、美观的 CSS 样式
        css_style = """
        <style>
            :root {
                --primary-color: #2563eb;
                --text-color: #334155;
                --bg-color: #f8fafc;
                --card-bg: #ffffff;
                --border-color: #e2e8f0;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                background-color: var(--bg-color);
                margin: 0;
                padding: 2rem;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background-color: var(--card-bg);
                padding: 3rem;
                border-radius: 12px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            }
            h1, h2, h3, h4, h5, h6 {
                color: #1e293b;
                margin-top: 1.5em;
                margin-bottom: 0.5em;
                font-weight: 700;
                line-height: 1.2;
            }
            h1 { font-size: 2.25rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.3em; }
            h2 { font-size: 1.8rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.3em; }
            h3 { font-size: 1.5rem; }
            p { margin-bottom: 1em; }
            a { color: var(--primary-color); text-decoration: none; }
            a:hover { text-decoration: underline; }
            code {
                background-color: #f1f5f9;
                padding: 0.2em 0.4em;
                border-radius: 4px;
                font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
                font-size: 0.9em;
                color: #ef4444;
            }
            pre {
                background-color: #1e293b;
                color: #f8fafc;
                padding: 1rem;
                border-radius: 8px;
                overflow-x: auto;
                margin-bottom: 1.5em;
            }
            pre code {
                background-color: transparent;
                color: inherit;
                padding: 0;
                font-size: 0.9em;
            }
            blockquote {
                border-left: 4px solid var(--primary-color);
                margin: 1.5em 0;
                padding-left: 1em;
                color: #64748b;
                font-style: italic;
                background-color: #f8fafc;
                padding: 1rem;
                border-radius: 0 8px 8px 0;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 1.5em;
            }
            th, td {
                border: 1px solid var(--border-color);
                padding: 0.75rem;
                text-align: left;
            }
            th {
                background-color: #f1f5f9;
                font-weight: 600;
            }
            tr:nth-child(even) {
                background-color: #f8fafc;
            }
            img {
                max-width: 100%;
                height: auto;
                border-radius: 8px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }
            hr {
                border: 0;
                border-top: 1px solid var(--border-color);
                margin: 2rem 0;
            }
            ul, ol {
                padding-left: 1.5rem;
                margin-bottom: 1.5em;
            }
            li {
                margin-bottom: 0.5em;
            }
            @media (max-width: 640px) {
                body { padding: 1rem; }
                .container { padding: 1.5rem; }
                h1 { font-size: 1.8rem; }
            }
        </style>
        """
        
        # 构建完整的 HTML 文档
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename}</title>
    {css_style}
</head>
<body>
    <div class="container">
        {html_body}
    </div>
</body>
</html>"""
        
        # 创建字节流
        html_bytes = full_html.encode('utf-8')
        
        # 将 HTML 作为 blob 消息返回
        yield self.create_blob_message(
            blob=html_bytes, 
            meta={'mime_type': 'text/html', 'filename': f"{filename}.html"}
        )
