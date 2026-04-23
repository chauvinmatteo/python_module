import sys
import importlib.util
import importlib.metadata


def main() -> None:

    try:
        missing: list[str] = [p for p in ["pandas", "numpy", "matplotlib"]
                              if importlib.util.find_spec(p) is None]
        if missing:
            raise ImportError(f"Missing modules: {', '.join(missing)}")
        import pandas as pd  # type: ignore[import-untyped]
        import numpy as np  # type: ignore[import-untyped]
        import matplotlib.pyplot as plt  # type: ignore[import-untyped]
    except ImportError as e:

        print("CRITICAL ERROR: "
              "Matrix connection failed due to missing dependencies.")
        print(f"Details: {e}\n")

        print("Please install the required packages "
              "using one of the following methods:\n")

        print("- Using pip")
        print("  1. Activate your virtual environment: "
              "source matrix_env/bin/activate")
        print("  2. Install from requirements: "
              "pip install -r requirements.txt")
        print("  3. Run the script: python3 loading.py\n")

        print("- Using Poetry")
        print("  1. Install dependencies: poetry install")
        print("  2. Run the script: poetry run python loading.py")

        sys.exit(1)

    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies")
    packages_info: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }

    for package, description in packages_info.items():
        version: str = importlib.metadata.version(package)
        print(f"[OK] {package} ({version}) - {description}")

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    data = np.random.rand(1000)
    df = pd.DataFrame(data, columns=["Matrix Signal"])

    plt.plot(df["Matrix Signal"])
    plt.title("Matrix Data Analysis")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
