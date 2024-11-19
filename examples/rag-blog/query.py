import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

load_dotenv()

def main():
    print("🚀 Starting the retrieval process...")

    index_name = os.environ.get("RAG_BLOG_INDEX_NAME")

    # Initialize embeddings and LLM
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()

    # Define the query
    query = "Give me project structure to dockerize PHP application."
    print(f"🔍 Query: {query}")

    # Initialize the vector store
    print("📦 Connecting to Pinecone vector store...")
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

    # Load retrieval-qa-chat prompt from hub
    print("🌐 Pulling retrieval-qa-chat prompt from hub...")
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    # Create chains for document combination and retrieval
    print("🔗 Setting up retrieval and combination chains...")
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(
        retriever=vectorstore.as_retriever(), combine_docs_chain=combine_docs_chain
    )

    # Execute the retrieval chain
    print("🧾 Running the retrieval chain...")
    retrieval_result = retrieval_chain.invoke(input={"input": query})
    print(f"📚 Retrieved Response:\n{retrieval_result['answer']}")


if __name__ == "__main__":
    main()
