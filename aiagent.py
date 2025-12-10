
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from typing import Annotated, Literal, TypedDict
from langgraph.graph.message import add_messages
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


# model = ChatOpenAI(
#     model="anthropic/claude-3.7-sonnet:thinking",
#     temperature=0.1,
#     openai_api_key=api_key,
#     base_url="https://openrouter.ai/api/v1"
# )
model = ChatOpenAI(
    model="gpt-4o-mini",  # <--- تغییر مهم: استفاده از مدل سبک و ارزان OpenAI
    temperature=0,
    openai_api_key=api_key,
    base_url = "https://openrouter.ai/api/v1",
)



@tool
def get_weather(city: str) -> str:
    """Get the current weather for a specific city."""
    # اینجا در یک برنامه واقعی به API هواشناسی وصل می‌شوید
    return f"Sunny and 25°C in {city}."


tools = [get_weather]
# متصل کردن ابزارها به مدل (تا مدل بداند این ابزارها وجود دارند)
model_with_tools = model.bind_tools(tools)


# 4. تعریف وضعیت (State)
# استفاده از add_messages باعث می‌شود پیام‌های جدید به لیست قبلی اضافه شوند (حافظه)
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


# 5. تعریف نودها (Nodes)
def agent_node(state: AgentState):
    """نود هوش مصنوعی که تصمیم می‌گیرد جواب دهد یا ابزار صدا بزند"""
    messages = state["messages"]
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}



tool_node = ToolNode(tools)


def should_continue(state: AgentState) -> Literal["tools", END]:
    """شرط برای تشخیص اینکه آیا مدل می‌خواهد ابزار صدا بزند یا خیر"""
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return END


# 6. ساخت گراف (Workflow)
workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "agent")

# شرط: اگر مدل ابزار خواست -> برو به tools، وگرنه -> تمام
workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge("tools", "agent")  # بعد از اجرای ابزار، دوباره برگرد به ایجنت تا نتیجه را تفسیر کند

# 7. اضافه کردن حافظه موقت (In-Memory)
checkpointer = MemorySaver()

# کامپایل کردن ایجنت با حافظه
app_agent = workflow.compile(checkpointer=checkpointer)

# 8. راه اندازی FastAPI
app = FastAPI()


class ChatRequest(BaseModel):
    text: str
    thread_id: str = "default_user"  # شناسه برای تشخیص کاربر/مکالمه


@app.post("/chat")
async def chat(request: ChatRequest):
    # تنظیم کانفیگ برای حافظه (هر thread_id یک حافظه جداگانه دارد)
    config = {"configurable": {"thread_id": request.thread_id}}

    # پیام کاربر
    input_message = HumanMessage(content=request.text)

    # اجرای ایجنت
    # stream_mode="values" آخرین وضعیت پیام‌ها را برمی‌گرداند
    final_state = app_agent.invoke(
        {"messages": [input_message]},
        config=config
    )

    # آخرین پیام (که جواب نهایی مدل است)
    last_message = final_state["messages"][-1].content
    return {"response": last_message}


@app.get("/")
def root():
    return {"message": "AI Agent with Memory is running!"}

if __name__ == "__main__":
    uvicorn.run("aiagent:app", host="127.0.0.1", port=8000, reload=True)