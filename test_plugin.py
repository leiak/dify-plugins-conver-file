"""
Test script to verify the Dify plugin structure and imports
"""
import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        from dify_plugin import Plugin, DifyPluginEnv
        print("✅ dify_plugin imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import dify_plugin: {e}")
        return False
    
    try:
        from dify_plugin.interfaces.tool import ToolProvider
        print("✅ ToolProvider imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import ToolProvider: {e}")
        return False
    
    try:
        from dify_plugin import Tool
        from dify_plugin.entities.tool import ToolInvokeMessage
        print("✅ Tool and ToolInvokeMessage imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Tool/ToolInvokeMessage: {e}")
        return False
    
    return True

def test_tool_classes():
    """Test if tool classes can be imported"""
    print("\nTesting tool classes...")
    
    # Add tools directory to path
    tools_path = os.path.join(os.path.dirname(__file__), 'tools')
    sys.path.insert(0, tools_path)
    
    try:
        from convert_md_to_pdf import ConvertMdToPdfTool
        print("✅ ConvertMdToPdfTool imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import ConvertMdToPdfTool: {e}")
        return False
    
    try:
        from convert_md_to_docx import ConvertMdToDocxTool
        print("✅ ConvertMdToDocxTool imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import ConvertMdToDocxTool: {e}")
        return False

    try:
        from convert_md_to_pptx import ConvertMdToPptxTool
        print("✅ ConvertMdToPptxTool imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import ConvertMdToPptxTool: {e}")
        return False

    try:
        from convert_md_to_txt import ConvertMdToTxtTool
        print("✅ ConvertMdToTxtTool imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import ConvertMdToTxtTool: {e}")
        return False

    try:
        from convert_md_to_html import ConvertMdToHtmlTool
        print("✅ ConvertMdToHtmlTool imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import ConvertMdToHtmlTool: {e}")
        return False
    
    return True

def test_provider_class():
    """Test if provider class can be imported"""
    print("\nTesting provider class...")
    
    # Add provider directory to path
    provider_path = os.path.join(os.path.dirname(__file__), 'provider')
    sys.path.insert(0, provider_path)
    
    try:
        from file_converter import FileConverterProvider
        print("✅ FileConverterProvider imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import FileConverterProvider: {e}")
        return False
    
    return True

def test_yaml_files():
    """Test if YAML files exist and are readable"""
    print("\nTesting YAML files...")
    
    yaml_files = [
        'manifest.yaml',
        'provider/file_converter.yaml',
        'tools/convert_md_to_pdf.yaml',
        'tools/convert_md_to_docx.yaml',
        'tools/convert_md_to_pptx.yaml',
        'tools/convert_md_to_txt.yaml',
        'tools/convert_md_to_html.yaml'
    ]
    
    base_path = os.path.dirname(__file__)
    all_exist = True
    
    for yaml_file in yaml_files:
        full_path = os.path.join(base_path, yaml_file)
        if os.path.exists(full_path):
            print(f"✅ {yaml_file} exists")
        else:
            print(f"❌ {yaml_file} not found")
            all_exist = False
    
    return all_exist

def main():
    print("=" * 60)
    print("Dify Plugin Structure Test")
    print("=" * 60)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Tool Classes", test_tool_classes()))
    results.append(("Provider Class", test_provider_class()))
    results.append(("YAML Files", test_yaml_files()))
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("🎉 All tests passed! Plugin structure is correct.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
