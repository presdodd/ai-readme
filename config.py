MAX_LINES_PER_FILE = 500

OPENAI_MODEL = "gpt-4.1"

README_FILENAME = "README.md"

DEFAULT_EXTENSIONS = [
    # Source code
    '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.go', '.rb', '.php', '.cpp', '.c', '.cs', '.rs',
    
    # Configuration and metadata
    '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.env',
    
    # Docs
    '.md', '.rst', '.txt', 'README',

    # Shell and scripting
    '.sh', '.bash', '.bat', '.ps1',

    # Containers, infra
    'Dockerfile', 'docker-compose.yml', '.tf', '.tf.json',
    
    # Dependency files
    'requirements.txt', 'package.json', 'Pipfile', 'pyproject.toml', 'environment.yml',
]