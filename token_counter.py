import os

from gpt3_tokenizer import encode


def should_exclude(path):
    exclude_dirs = {
        "node_modules",
        "output",
        "dist",
        "__pycache__",
        ".git",
        ".aider.tags.cache.v3",
        ".vscode",
        "coverage",
        "__test__",
        "pipelines",
    }
    exclude_extensions = {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".tiff",
        ".zip",
        ".tar",
        ".gz",
        ".rar",
        ".7z",
        ".exe",
        ".dll",
        ".so",
        ".dylib",
        ".pyc",
        ".pyo",
        ".pyd",
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".md",
    }
    exclude_files = {
        "package-lock.json",
        "yarn.lock",
        ".gitignore",
        ".dockerignore",
        ".env",
        ".DS_Store",
        ".editorconfig",
        "azure-pipelines.yml",
        "LICENSE",
        "jest.config.js",
        "tsconfig.json",
    }

    parts = path.split(os.sep)
    if any(part in exclude_dirs for part in parts):
        return True

    filename = os.path.basename(path)
    if filename in exclude_files:
        return True

    _, ext = os.path.splitext(path.lower())
    return ext in exclude_extensions


def count_tokens_in_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        tokens = encode(content)
        return len(tokens)
    except Exception as e:
        print(f"Error processing file: {file_path}. Error: {str(e)}")
        return 0


def count_tokens_in_directory(directory_path):
    file_tokens = []
    for root, dirs, files in os.walk(directory_path):
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
        for file in files:
            file_path = os.path.join(root, file)
            if not should_exclude(file_path):
                tokens = count_tokens_in_file(file_path)
                file_tokens.append((file_path, tokens))

    file_tokens.sort(key=lambda x: x[1], reverse=True)
    total_tokens = sum(tokens for _, tokens in file_tokens)

    return file_tokens, total_tokens
