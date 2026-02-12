from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


from tools.md_to_csv.md_to_csv import MarkdownToCsvTool
from tools.md_to_docx.md_to_docx import MarkdownToDocxTool
from tools.md_to_pdf.md_to_pdf import MarkdownToPdfTool
from tools.md_to_xlsx.md_to_xlsx import MarkdownToXlsxTool


class Markdown2SuiteProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            """
            IMPLEMENT YOUR VALIDATION HERE
            """
            tools = [
                MarkdownToCsvTool,
                MarkdownToDocxTool,
                MarkdownToPdfTool,
                MarkdownToXlsxTool,
            ]
            for tool in tools:
                tool.from_credentials({})
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))

