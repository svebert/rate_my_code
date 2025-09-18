from pathlib import Path
from rate_my_code import rate_my_code


def main():
    # Pfad zum eigenen Package (relativ zum Demo-Skript)
    package_path = Path(__file__).parent / ".."
    print(package_path)
    # Analysiere das Package
    result = rate_my_code(package_path, excludes=[".venv", ".idea"])

    print("\n--- Einzelne Dateien ---")
    for f, info in result["files"].items():
        print(f"\nDatei: {f}")
        print(f"  Score: {info['score']}")
        print(f"  Länge: {info['length']} Zeichen")
        if info["comments"]:
            print(f"  Hinweise: {', '.join(info['comments'])}")
        else:
            print("  Hinweise: Keine")

    print("\n--- Gesamt ---")
    print(f"Gewichteter Gesamt-Score: {result['score']:.2f}")
    print(
        f"Alle Hinweise gesammelt: "
        f"{', '.join(result['comments']) if result['comments'] else 'Keine'}"
    )


if __name__ == "__main__":
    main()
