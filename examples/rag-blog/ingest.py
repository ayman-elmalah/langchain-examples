import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_pinecone import PineconeVectorStore

# Load environment variables
load_dotenv()


def main():
    print("🚀 Starting document ingestion...")

    # Get the absolute path to the file relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
    file_name = "blog.txt"
    file_path = os.path.join(script_dir, file_name)

    print(f"📄 Loading document from: {file_path}")

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    loader = TextLoader(file_path)
    document = loader.load()

    # Split the document into manageable chunks
    print("✂️ Splitting document into chunks...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"✅ Created {len(texts)} chunks.")

    # Generate embeddings
    print("🧠 Generating embeddings...")
    embeddings = OpenAIEmbeddings()

    # Store embeddings in Pinecone
    index_name = os.environ.get("RAG_BLOG_INDEX_NAME")
    print(f"📦 Storing embeddings in Pinecone index: {index_name}")
    vector_store = PineconeVectorStore(index=index_name, embedding=embeddings)
    vector_store.from_documents(texts, embeddings, index_name=index_name)

    print("🎉 Ingestion process completed!")


if __name__ == "__main__":
    main()
