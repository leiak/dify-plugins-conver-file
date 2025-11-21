# Dify 文件转换插件（dify-plugins-conver-file）

## 项目概述

`dify-plugins-conver-file` 是一个基于 Dify 平台的 **文件转换插件**，用于在 Dify 工作流中实现多种文档格式之间的相互转换。插件目前已实现的转换功能包括：
- Markdown → PDF
- Markdown → DOCX
- Markdown → PPTX
- Markdown → TXT
- Markdown → HTML

插件遵循 Dify 插件规范，提供统一的 **Tool** 接口，可在 Dify 的工具链中直接调用，实现自动化的文档处理。

## 功能特性

- **多格式支持**：支持常见的文档格式相互转换，满足不同业务场景需求。
- **高可配置**：通过 `manifest.yaml` 可灵活配置插件的入口、参数及元信息。
- **易于集成**：遵循 Dify 插件标准，使用 `provider` 与 `tool` 配置即可在 Dify 中直接使用。
- **可扩展**：代码结构清晰，便于后续添加新的转换工具（如 PDF → Markdown 等）。

## 安装与使用

1. **安装依赖**（在插件根目录执行）
   ```bash
   pip install -r requirements.txt
   ```
2. **启动插件服务**（确保已在 Dify 平台上注册插件）
   ```bash
   python -m dify_plugins_conver_file.main
   ```
