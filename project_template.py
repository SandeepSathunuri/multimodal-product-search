import os
from pathlib import Path
import yaml

PROJECT_NAME = "multimodal-product-search"

# Folder structure
folders = [
    "configs",
    "data/raw",
    "data/processed",
    "data/embeddings",
    "notebooks",
    "scripts/preprocess",
    "scripts/build_index",
    "scripts/search",
    "agents",
    "app",
    "assets",
    "logs",
    "tests"
]

# Files to create: {relative_path: content}
files = {
    ".gitignore": """__pycache__/
*.pyc
*.pkl
*.npy
*.pt
.DS_Store
.env
logs/
""",
    "README.md": f"# {PROJECT_NAME}\n\n🔍 A powerful open-source multimodal product search and recommendation engine using text, images, and voice.",
    "requirements.txt": """torch
faiss-cpu
pandas
numpy
sentence-transformers
transformers
Pillow
tqdm
pyyaml
gradio
streamlit
fastapi
uvicorn
""",
    "configs/config.yaml": {
        "project": {"name": PROJECT_NAME},
        "paths": {
            "raw_data_csv": "data/raw/data.csv",
            "raw_image_dir": "data/raw/images",
            "cleaned_csv": "data/processed/cleaned_data.csv",
            "aligned_csv": "data/processed/aligned_preprocessed.csv",
            "text_embeddings": "data/embeddings/text_embeddings.npy",
            "image_embeddings": "data/embeddings/image_embeddings_clip.npy",
            "fused_embeddings": "data/embeddings/fused_embeddings.npy",
            "faiss_fusion_index": "data/embeddings/fused_index.faiss"
        },
        "models": {
            "text_model": "all-MiniLM-L6-v2",
            "image_model": "openai/clip-vit-base-patch32"
        },
        "fusion": {"alpha": 0.5, "beta": 0.5}
    },
    "main.py": '''"""
Entry point to orchestrate modules
"""
print("🔧 Multimodal Product Search CLI under construction...")
'''
}


def create_project_structure(base_path):
    print(f"📁 Creating project: {PROJECT_NAME}")
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"  ✅ Folder created: {path}")

    for rel_path, content in files.items():
        path = os.path.join(base_path, rel_path)
        with open(path, "w", encoding="utf-8") as f:
            if isinstance(content, dict):  # YAML config
                yaml.dump(content, f, sort_keys=False)
            else:
                f.write(content)
        print(f"  📄 File created: {path}")


if __name__ == "__main__":
    current_dir = os.getcwd()
    project_path = os.path.join(current_dir, PROJECT_NAME)
    os.makedirs(project_path, exist_ok=True)
    create_project_structure(project_path)
    print("\n✅ Project scaffold complete. You can now `cd` into it and start building!")
