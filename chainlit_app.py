import chainlit as cl
from langchain_core.runnables import RunnableParallel

# from app import rag_chain

# System message with typing animation
WELCOME_MESSAGE = """👋 Welcome to the **Kitchener City Assistant**! 

I can help you with:
- Municipal services
- Building permits
- Recycling programs
- City bylaws
- And more!

Ask me anything about Kitchener's city services..."""


from chainlit import AskUserMessage, Message, on_chat_start


@cl.on_chat_start
async def main():
    res = await AskUserMessage(content="What is your name?", timeout=30).send()
    if res:
        await Message(
            content=f"Your name is: {res['content']}.\nChainlit installation is working!\nYou can now start building your own chainlit apps!",
        ).send()

@cl.on_message
async def on_message(msg: cl.Message):
    print("The user sent: ", msg.content)





# @cl.on_chat_start
# async def on_chat_start():
#     """Initialize the chat session with custom UI elements"""
#     # Set up avatar and headers
#     # await cl.Avatar(
#     #     name="Kitchener Bot",
#     #     url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vectorstock.com%2Froyalty-free-vector%2Fbot-sign-design-robot-logo-template-modern-flat-vector-27973154&psig=AOvVaw2lEwnofBiqSpkvOkWVwnku&ust=1743435767915000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKj20r-SsowDFQAAAAAdAAAAABAE"
#     # ).send()
    
#     # Create expandable introduction
#     intro = cl.Text(content=WELCOME_MESSAGE, display="page")
#     await intro.send()
    
#     # Store the chain in user session
#     cl.user_session.set("chain", rag_chain)

# @cl.on_message
# async def handle_message(message: cl.Message):
#     """Process incoming messages with enhanced UI"""
#     chain = cl.user_session.get("chain")
    
#     # Create a loading spinner
#     msg = cl.Message(content="")
#     await msg.send()
    
#     try:
#         # Stream response with sources
#         full_response = ""
#         sources = []
        
#         async for chunk in chain.astream(message.content):
#             if "answer" in chunk:
#                 await msg.stream_token(chunk["answer"])
#                 full_response += chunk["answer"]
#             if "sources" in chunk:
#                 sources.extend(chunk["sources"])
        
#         # Add verified sources if available
#         if sources:
#             source_elements = [
#                 cl.Text(name="Source", content=f"🔗 {source}", display="side")
#                 for source in sorted(set(sources))
#             ]
            
#             await cl.Message(
#                 content="Verified Sources:",
#                 elements=source_elements,
#                 parent_id=msg.id
#             ).send()
            
#         # Finalize the message
#         await msg.update()
        
#     except Exception as e:
#         await cl.Message(
#             content=f"⚠️ Error: {str(e)}\nPlease try again or rephrase your question."
#         ).send()
#         print(f"Error processing message: {e}")