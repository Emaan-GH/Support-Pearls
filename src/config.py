import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-5.6-luna")
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "text-embedding-3-small"
    )

    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "800"))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "120"))

    TOP_K = int(os.getenv("TOP_K", "4"))
    SIMILARITY_THRESHOLD = float(
        os.getenv("SIMILARITY_THRESHOLD", "0.35")
    )

    DATA_DIR = os.getenv(
        "DATA_DIR",
        "data/knowledge_base"
    )

    VECTOR_DIR = os.getenv(
        "VECTOR_DIR",
        "data/vector_store"
    )

    MAX_HISTORY = int(
        os.getenv("MAX_HISTORY", "6")
    )


settings = Settings()