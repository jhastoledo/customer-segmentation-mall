"""
Instalação do pacote src/ como pacote editável.

Uso:
    pip install -e .

Substitua os campos marcados com [colchetes] antes de publicar.
"""

from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="customer_segmentation_mall",          
    version="0.1.0",
    author="Jhonnes Toledo",
    author_email="255188448+jhastoledo@users.noreply.github.com",
    description="Projeto - Segmentação de clientes - Shopping",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhastoledo",
    packages=find_packages(exclude=["tests*", "notebooks*"]),
    python_requires=">=3.10",
    install_requires=[
        "pandas>=2.0",
        "numpy>=1.24",
        "scikit-learn>=1.3",
        "xgboost>=2.0",
        "matplotlib>=3.7",
        "seaborn>=0.12",
        "joblib>=1.3",
        "pyyaml>=6.0",
        "python-dotenv>=1.0",
        "shap>=0.43",
        "statsmodels>=0.14",
        "streamlit>=1.30",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "isort>=5.0",
            "flake8>=6.0",
            "ipykernel>=6.0",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
