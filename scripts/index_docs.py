from rag.indexer import RagIndexer


def main():
    indexer = RagIndexer()
    count = indexer.build()
    print(f"✅ Indexed {count} PDFs into Chroma")


if __name__ == "__main__":
    main()
