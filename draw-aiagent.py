from aiagent import app_agent
from langchain_core.runnables.graph import MermaidDrawMethod

# نام فایل خروجی
filename = "agent_graph.png"

print("...")

try:
    # تبدیل گراف به تصویر PNG
    png_data = app_agent.get_graph().draw_mermaid_png(
        draw_method=MermaidDrawMethod.API,
    )

    # ذخیره فایل
    with open(filename, "wb") as f:
        f.write(png_data)

    print(f" گراف با موفقیت در فایل '{filename}' ذخیره شد.")

except Exception as e:
    print(" error")
    print(e)
    print("\nنکته: برای ذخیره عکس نیاز به اینترنت دارید تا از API Mermaid استفاده شود.")