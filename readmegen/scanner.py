import os
from typing import List
from config import DEFAULT_EXTENSIONS, MAX_LINES_PER_FILE

def walk(dir: str, extensions: List[str] = None) -> List[str]:
    extensions = extensions or DEFAULT_EXTENSIONS
    result = []

    for dirpath, dirnames, filenames in os.walk(dir):
        # Exclude hidden folders and files
        filenames = [f for f in filenames if not f[0] == '.']
        dirnames[:] = [d for d in dirnames if not d[0] == '.']

        for name in filenames:
            if any(name.endswith(ext) for ext in extensions
                   or name in extensions):
                s = "===--------- " + name + " ---------===\n"
                f = open(dirpath + "/" + name)
                s += f.read(MAX_LINES_PER_FILE)
                result.append(s)

    return result

def build_context(dir: str, extensions: List[str] = None) -> str:
    files = walk(dir, extensions)
    context = "# Project File Summaries\n\n"
    for f in files:
        context += f

    return context