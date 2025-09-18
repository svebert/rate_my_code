from pathlib import Path
from rate_my_code import rate_my_code

result = rate_my_code(Path("example_code"))

for r in result["files"]:
    print(f"{r}: {result['files'][r]}")
