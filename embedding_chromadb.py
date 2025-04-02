{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4",
      "machine_shape": "hm"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "# Checking whether my runtime has GPU or not."
      ],
      "metadata": {
        "id": "1wCoXFw_rc_F"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import torch\n",
        "print(\"GPU Available:\", torch.cuda.is_available())\n",
        "print(\"GPU Name:\", torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"No GPU detected\")\n"
      ],
      "metadata": {
        "id": "CxrvgQMrr9gc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f7a8dcc2-b90f-4aab-f980-659866fc4589"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "GPU Available: True\n",
            "GPU Name: Tesla T4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install sentence_transformers -q"
      ],
      "metadata": {
        "id": "yTJKk6c3Psdx"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install chromadb"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "6k2uYqZ5ORT0",
        "outputId": "2db51d3a-34d8-461e-928a-fa69d6eda7de"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: chromadb in /usr/local/lib/python3.11/dist-packages (0.6.3)\n",
            "Requirement already satisfied: build>=1.0.3 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.2.2.post1)\n",
            "Requirement already satisfied: pydantic>=1.9 in /usr/local/lib/python3.11/dist-packages (from chromadb) (2.10.6)\n",
            "Requirement already satisfied: chroma-hnswlib==0.7.6 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.7.6)\n",
            "Requirement already satisfied: fastapi>=0.95.2 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.115.12)\n",
            "Requirement already satisfied: uvicorn>=0.18.3 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.34.0)\n",
            "Requirement already satisfied: numpy>=1.22.5 in /usr/local/lib/python3.11/dist-packages (from chromadb) (2.0.2)\n",
            "Requirement already satisfied: posthog>=2.4.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (3.21.0)\n",
            "Requirement already satisfied: typing_extensions>=4.5.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (4.12.2)\n",
            "Requirement already satisfied: onnxruntime>=1.14.1 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.21.0)\n",
            "Requirement already satisfied: opentelemetry-api>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.31.1)\n",
            "Requirement already satisfied: opentelemetry-exporter-otlp-proto-grpc>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.31.1)\n",
            "Requirement already satisfied: opentelemetry-instrumentation-fastapi>=0.41b0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.52b1)\n",
            "Requirement already satisfied: opentelemetry-sdk>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.31.1)\n",
            "Requirement already satisfied: tokenizers>=0.13.2 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.21.1)\n",
            "Requirement already satisfied: pypika>=0.48.9 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.48.9)\n",
            "Requirement already satisfied: tqdm>=4.65.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (4.67.1)\n",
            "Requirement already satisfied: overrides>=7.3.1 in /usr/local/lib/python3.11/dist-packages (from chromadb) (7.7.0)\n",
            "Requirement already satisfied: importlib-resources in /usr/local/lib/python3.11/dist-packages (from chromadb) (6.5.2)\n",
            "Requirement already satisfied: grpcio>=1.58.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.71.0)\n",
            "Requirement already satisfied: bcrypt>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from chromadb) (4.3.0)\n",
            "Requirement already satisfied: typer>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.15.2)\n",
            "Requirement already satisfied: kubernetes>=28.1.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (32.0.1)\n",
            "Requirement already satisfied: tenacity>=8.2.3 in /usr/local/lib/python3.11/dist-packages (from chromadb) (9.0.0)\n",
            "Requirement already satisfied: PyYAML>=6.0.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (6.0.2)\n",
            "Requirement already satisfied: mmh3>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from chromadb) (5.1.0)\n",
            "Requirement already satisfied: orjson>=3.9.12 in /usr/local/lib/python3.11/dist-packages (from chromadb) (3.10.15)\n",
            "Requirement already satisfied: httpx>=0.27.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.28.1)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (13.9.4)\n",
            "Requirement already satisfied: packaging>=19.1 in /usr/local/lib/python3.11/dist-packages (from build>=1.0.3->chromadb) (24.2)\n",
            "Requirement already satisfied: pyproject_hooks in /usr/local/lib/python3.11/dist-packages (from build>=1.0.3->chromadb) (1.2.0)\n",
            "Requirement already satisfied: starlette<0.47.0,>=0.40.0 in /usr/local/lib/python3.11/dist-packages (from fastapi>=0.95.2->chromadb) (0.46.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx>=0.27.0->chromadb) (4.9.0)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx>=0.27.0->chromadb) (2025.1.31)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx>=0.27.0->chromadb) (1.0.7)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from httpx>=0.27.0->chromadb) (3.10)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx>=0.27.0->chromadb) (0.14.0)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (1.17.0)\n",
            "Requirement already satisfied: python-dateutil>=2.5.3 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (2.8.2)\n",
            "Requirement already satisfied: google-auth>=1.0.1 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (2.38.0)\n",
            "Requirement already satisfied: websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (1.8.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (2.32.3)\n",
            "Requirement already satisfied: requests-oauthlib in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (2.0.0)\n",
            "Requirement already satisfied: oauthlib>=3.2.2 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (3.2.2)\n",
            "Requirement already satisfied: urllib3>=1.24.2 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (2.3.0)\n",
            "Requirement already satisfied: durationpy>=0.7 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (0.9)\n",
            "Requirement already satisfied: coloredlogs in /usr/local/lib/python3.11/dist-packages (from onnxruntime>=1.14.1->chromadb) (15.0.1)\n",
            "Requirement already satisfied: flatbuffers in /usr/local/lib/python3.11/dist-packages (from onnxruntime>=1.14.1->chromadb) (25.2.10)\n",
            "Requirement already satisfied: protobuf in /usr/local/lib/python3.11/dist-packages (from onnxruntime>=1.14.1->chromadb) (5.29.4)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.11/dist-packages (from onnxruntime>=1.14.1->chromadb) (1.13.1)\n",
            "Requirement already satisfied: deprecated>=1.2.6 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-api>=1.2.0->chromadb) (1.2.18)\n",
            "Requirement already satisfied: importlib-metadata<8.7.0,>=6.0 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-api>=1.2.0->chromadb) (8.6.1)\n",
            "Requirement already satisfied: googleapis-common-protos~=1.52 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.69.2)\n",
            "Requirement already satisfied: opentelemetry-exporter-otlp-proto-common==1.31.1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.31.1)\n",
            "Requirement already satisfied: opentelemetry-proto==1.31.1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.31.1)\n",
            "Requirement already satisfied: opentelemetry-instrumentation-asgi==0.52b1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.52b1)\n",
            "Requirement already satisfied: opentelemetry-instrumentation==0.52b1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.52b1)\n",
            "Requirement already satisfied: opentelemetry-semantic-conventions==0.52b1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.52b1)\n",
            "Requirement already satisfied: opentelemetry-util-http==0.52b1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.52b1)\n",
            "Requirement already satisfied: wrapt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation==0.52b1->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (1.17.2)\n",
            "Requirement already satisfied: asgiref~=3.0 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-asgi==0.52b1->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (3.8.1)\n",
            "Requirement already satisfied: monotonic>=1.5 in /usr/local/lib/python3.11/dist-packages (from posthog>=2.4.0->chromadb) (1.6)\n",
            "Requirement already satisfied: backoff>=1.10.0 in /usr/local/lib/python3.11/dist-packages (from posthog>=2.4.0->chromadb) (2.2.1)\n",
            "Requirement already satisfied: distro>=1.5.0 in /usr/local/lib/python3.11/dist-packages (from posthog>=2.4.0->chromadb) (1.9.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic>=1.9->chromadb) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic>=1.9->chromadb) (2.27.2)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->chromadb) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->chromadb) (2.18.0)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.16.4 in /usr/local/lib/python3.11/dist-packages (from tokenizers>=0.13.2->chromadb) (0.29.3)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.11/dist-packages (from typer>=0.9.0->chromadb) (8.1.8)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from typer>=0.9.0->chromadb) (1.5.4)\n",
            "Requirement already satisfied: httptools>=0.6.3 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.6.4)\n",
            "Requirement already satisfied: python-dotenv>=0.13 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (1.0.1)\n",
            "Requirement already satisfied: uvloop!=0.15.0,!=0.15.1,>=0.14.0 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.21.0)\n",
            "Requirement already satisfied: watchfiles>=0.13 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (1.0.4)\n",
            "Requirement already satisfied: websockets>=10.4 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (15.0.1)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (5.5.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.11/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (0.4.1)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.11/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (4.9)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb) (3.18.0)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers>=0.13.2->chromadb) (2025.3.0)\n",
            "Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.11/dist-packages (from importlib-metadata<8.7.0,>=6.0->opentelemetry-api>=1.2.0->chromadb) (3.21.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->chromadb) (0.1.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->kubernetes>=28.1.0->chromadb) (3.4.1)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx>=0.27.0->chromadb) (1.3.1)\n",
            "Requirement already satisfied: humanfriendly>=9.1 in /usr/local/lib/python3.11/dist-packages (from coloredlogs->onnxruntime>=1.14.1->chromadb) (10.0)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from sympy->onnxruntime>=1.14.1->chromadb) (1.3.0)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.4.6 in /usr/local/lib/python3.11/dist-packages (from pyasn1-modules>=0.2.1->google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (0.6.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# The second command installs ChromaDB and sentence-transformers for embedding storage.\n",
        "\n",
        "!pip install chromadb sentence-transformers"
      ],
      "metadata": {
        "collapsed": true,
        "id": "VNrs_JAXsMK4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "eb09d591-c59e-4c34-febe-4028ad2fbec4"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: chromadb in /usr/local/lib/python3.11/dist-packages (0.6.3)\n",
            "Requirement already satisfied: sentence-transformers in /usr/local/lib/python3.11/dist-packages (3.4.1)\n",
            "Requirement already satisfied: build>=1.0.3 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.2.2.post1)\n",
            "Requirement already satisfied: pydantic>=1.9 in /usr/local/lib/python3.11/dist-packages (from chromadb) (2.10.6)\n",
            "Requirement already satisfied: chroma-hnswlib==0.7.6 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.7.6)\n",
            "Requirement already satisfied: fastapi>=0.95.2 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.115.12)\n",
            "Requirement already satisfied: uvicorn>=0.18.3 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.34.0)\n",
            "Requirement already satisfied: numpy>=1.22.5 in /usr/local/lib/python3.11/dist-packages (from chromadb) (2.0.2)\n",
            "Requirement already satisfied: posthog>=2.4.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (3.21.0)\n",
            "Requirement already satisfied: typing_extensions>=4.5.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (4.12.2)\n",
            "Requirement already satisfied: onnxruntime>=1.14.1 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.21.0)\n",
            "Requirement already satisfied: opentelemetry-api>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.31.1)\n",
            "Requirement already satisfied: opentelemetry-exporter-otlp-proto-grpc>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.31.1)\n",
            "Requirement already satisfied: opentelemetry-instrumentation-fastapi>=0.41b0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.52b1)\n",
            "Requirement already satisfied: opentelemetry-sdk>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.31.1)\n",
            "Requirement already satisfied: tokenizers>=0.13.2 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.21.1)\n",
            "Requirement already satisfied: pypika>=0.48.9 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.48.9)\n",
            "Requirement already satisfied: tqdm>=4.65.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (4.67.1)\n",
            "Requirement already satisfied: overrides>=7.3.1 in /usr/local/lib/python3.11/dist-packages (from chromadb) (7.7.0)\n",
            "Requirement already satisfied: importlib-resources in /usr/local/lib/python3.11/dist-packages (from chromadb) (6.5.2)\n",
            "Requirement already satisfied: grpcio>=1.58.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (1.71.0)\n",
            "Requirement already satisfied: bcrypt>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from chromadb) (4.3.0)\n",
            "Requirement already satisfied: typer>=0.9.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.15.2)\n",
            "Requirement already satisfied: kubernetes>=28.1.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (32.0.1)\n",
            "Requirement already satisfied: tenacity>=8.2.3 in /usr/local/lib/python3.11/dist-packages (from chromadb) (9.0.0)\n",
            "Requirement already satisfied: PyYAML>=6.0.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (6.0.2)\n",
            "Requirement already satisfied: mmh3>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from chromadb) (5.1.0)\n",
            "Requirement already satisfied: orjson>=3.9.12 in /usr/local/lib/python3.11/dist-packages (from chromadb) (3.10.15)\n",
            "Requirement already satisfied: httpx>=0.27.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (0.28.1)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.11/dist-packages (from chromadb) (13.9.4)\n",
            "Requirement already satisfied: transformers<5.0.0,>=4.41.0 in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (4.49.0)\n",
            "Requirement already satisfied: torch>=1.11.0 in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (2.6.0+cu124)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (1.6.1)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (1.14.1)\n",
            "Requirement already satisfied: huggingface-hub>=0.20.0 in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (0.29.3)\n",
            "Requirement already satisfied: Pillow in /usr/local/lib/python3.11/dist-packages (from sentence-transformers) (11.1.0)\n",
            "Requirement already satisfied: packaging>=19.1 in /usr/local/lib/python3.11/dist-packages (from build>=1.0.3->chromadb) (24.2)\n",
            "Requirement already satisfied: pyproject_hooks in /usr/local/lib/python3.11/dist-packages (from build>=1.0.3->chromadb) (1.2.0)\n",
            "Requirement already satisfied: starlette<0.47.0,>=0.40.0 in /usr/local/lib/python3.11/dist-packages (from fastapi>=0.95.2->chromadb) (0.46.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx>=0.27.0->chromadb) (4.9.0)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx>=0.27.0->chromadb) (2025.1.31)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx>=0.27.0->chromadb) (1.0.7)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from httpx>=0.27.0->chromadb) (3.10)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx>=0.27.0->chromadb) (0.14.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from huggingface-hub>=0.20.0->sentence-transformers) (3.18.0)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub>=0.20.0->sentence-transformers) (2025.3.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from huggingface-hub>=0.20.0->sentence-transformers) (2.32.3)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (1.17.0)\n",
            "Requirement already satisfied: python-dateutil>=2.5.3 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (2.8.2)\n",
            "Requirement already satisfied: google-auth>=1.0.1 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (2.38.0)\n",
            "Requirement already satisfied: websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (1.8.0)\n",
            "Requirement already satisfied: requests-oauthlib in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (2.0.0)\n",
            "Requirement already satisfied: oauthlib>=3.2.2 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (3.2.2)\n",
            "Requirement already satisfied: urllib3>=1.24.2 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (2.3.0)\n",
            "Requirement already satisfied: durationpy>=0.7 in /usr/local/lib/python3.11/dist-packages (from kubernetes>=28.1.0->chromadb) (0.9)\n",
            "Requirement already satisfied: coloredlogs in /usr/local/lib/python3.11/dist-packages (from onnxruntime>=1.14.1->chromadb) (15.0.1)\n",
            "Requirement already satisfied: flatbuffers in /usr/local/lib/python3.11/dist-packages (from onnxruntime>=1.14.1->chromadb) (25.2.10)\n",
            "Requirement already satisfied: protobuf in /usr/local/lib/python3.11/dist-packages (from onnxruntime>=1.14.1->chromadb) (5.29.4)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.11/dist-packages (from onnxruntime>=1.14.1->chromadb) (1.13.1)\n",
            "Requirement already satisfied: deprecated>=1.2.6 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-api>=1.2.0->chromadb) (1.2.18)\n",
            "Requirement already satisfied: importlib-metadata<8.7.0,>=6.0 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-api>=1.2.0->chromadb) (8.6.1)\n",
            "Requirement already satisfied: googleapis-common-protos~=1.52 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.69.2)\n",
            "Requirement already satisfied: opentelemetry-exporter-otlp-proto-common==1.31.1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.31.1)\n",
            "Requirement already satisfied: opentelemetry-proto==1.31.1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-exporter-otlp-proto-grpc>=1.2.0->chromadb) (1.31.1)\n",
            "Requirement already satisfied: opentelemetry-instrumentation-asgi==0.52b1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.52b1)\n",
            "Requirement already satisfied: opentelemetry-instrumentation==0.52b1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.52b1)\n",
            "Requirement already satisfied: opentelemetry-semantic-conventions==0.52b1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.52b1)\n",
            "Requirement already satisfied: opentelemetry-util-http==0.52b1 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (0.52b1)\n",
            "Requirement already satisfied: wrapt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation==0.52b1->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (1.17.2)\n",
            "Requirement already satisfied: asgiref~=3.0 in /usr/local/lib/python3.11/dist-packages (from opentelemetry-instrumentation-asgi==0.52b1->opentelemetry-instrumentation-fastapi>=0.41b0->chromadb) (3.8.1)\n",
            "Requirement already satisfied: monotonic>=1.5 in /usr/local/lib/python3.11/dist-packages (from posthog>=2.4.0->chromadb) (1.6)\n",
            "Requirement already satisfied: backoff>=1.10.0 in /usr/local/lib/python3.11/dist-packages (from posthog>=2.4.0->chromadb) (2.2.1)\n",
            "Requirement already satisfied: distro>=1.5.0 in /usr/local/lib/python3.11/dist-packages (from posthog>=2.4.0->chromadb) (1.9.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic>=1.9->chromadb) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic>=1.9->chromadb) (2.27.2)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->chromadb) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich>=10.11.0->chromadb) (2.18.0)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (3.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (3.1.6)\n",
            "Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (12.4.127)\n",
            "Requirement already satisfied: nvidia-cuda-runtime-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (12.4.127)\n",
            "Requirement already satisfied: nvidia-cuda-cupti-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (12.4.127)\n",
            "Requirement already satisfied: nvidia-cudnn-cu12==9.1.0.70 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (9.1.0.70)\n",
            "Requirement already satisfied: nvidia-cublas-cu12==12.4.5.8 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (12.4.5.8)\n",
            "Requirement already satisfied: nvidia-cufft-cu12==11.2.1.3 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (11.2.1.3)\n",
            "Requirement already satisfied: nvidia-curand-cu12==10.3.5.147 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (10.3.5.147)\n",
            "Requirement already satisfied: nvidia-cusolver-cu12==11.6.1.9 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (11.6.1.9)\n",
            "Requirement already satisfied: nvidia-cusparse-cu12==12.3.1.170 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (12.3.1.170)\n",
            "Requirement already satisfied: nvidia-cusparselt-cu12==0.6.2 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (0.6.2)\n",
            "Requirement already satisfied: nvidia-nccl-cu12==2.21.5 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (2.21.5)\n",
            "Requirement already satisfied: nvidia-nvtx-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (12.4.127)\n",
            "Requirement already satisfied: nvidia-nvjitlink-cu12==12.4.127 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (12.4.127)\n",
            "Requirement already satisfied: triton==3.2.0 in /usr/local/lib/python3.11/dist-packages (from torch>=1.11.0->sentence-transformers) (3.2.0)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.11/dist-packages (from sympy->onnxruntime>=1.14.1->chromadb) (1.3.0)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.11/dist-packages (from transformers<5.0.0,>=4.41.0->sentence-transformers) (2024.11.6)\n",
            "Requirement already satisfied: safetensors>=0.4.1 in /usr/local/lib/python3.11/dist-packages (from transformers<5.0.0,>=4.41.0->sentence-transformers) (0.5.3)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.11/dist-packages (from typer>=0.9.0->chromadb) (8.1.8)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.11/dist-packages (from typer>=0.9.0->chromadb) (1.5.4)\n",
            "Requirement already satisfied: httptools>=0.6.3 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.6.4)\n",
            "Requirement already satisfied: python-dotenv>=0.13 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (1.0.1)\n",
            "Requirement already satisfied: uvloop!=0.15.0,!=0.15.1,>=0.14.0 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.21.0)\n",
            "Requirement already satisfied: watchfiles>=0.13 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (1.0.4)\n",
            "Requirement already satisfied: websockets>=10.4 in /usr/local/lib/python3.11/dist-packages (from uvicorn[standard]>=0.18.3->chromadb) (15.0.1)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn->sentence-transformers) (1.4.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn->sentence-transformers) (3.6.0)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (5.5.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.11/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (0.4.1)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.11/dist-packages (from google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (4.9)\n",
            "Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.11/dist-packages (from importlib-metadata<8.7.0,>=6.0->opentelemetry-api>=1.2.0->chromadb) (3.21.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->chromadb) (0.1.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->huggingface-hub>=0.20.0->sentence-transformers) (3.4.1)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx>=0.27.0->chromadb) (1.3.1)\n",
            "Requirement already satisfied: humanfriendly>=9.1 in /usr/local/lib/python3.11/dist-packages (from coloredlogs->onnxruntime>=1.14.1->chromadb) (10.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->torch>=1.11.0->sentence-transformers) (3.0.2)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.4.6 in /usr/local/lib/python3.11/dist-packages (from pyasn1-modules>=0.2.1->google-auth>=1.0.1->kubernetes>=28.1.0->chromadb) (0.6.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "EYpM5-UDwXrY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "186eb9b3-3690-4ab6-848c-77266bb15bb7"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "df=pd.read_parquet(r\"/content/drive/MyDrive/search_engine/files/subtitles_extracted.parquet\")\n"
      ],
      "metadata": {
        "id": "hNOKaQqKsMQ7"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "id": "WHEwEHhxwJck",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "outputId": "f0c6c2d6-df99-4569-d356-3ce5cd60b0c0"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                               chunk  \\\n",
              "0  Watch any video online with OpenSUBTITLES Free...   \n",
              "1  on Keep dancing Whatever Im kidding Dont get m...   \n",
              "2  And you Douche Handsome Conceited Just like yo...   \n",
              "3  that so Yes How long will this program run If ...   \n",
              "4  her Gramps Uncle Erning Aunt Elma this is Tep ...   \n",
              "\n",
              "                                            metadata  \n",
              "0  {'original_index': 0, 'subtitle_id': 9251120, ...  \n",
              "1  {'original_index': 0, 'subtitle_id': 9251120, ...  \n",
              "2  {'original_index': 0, 'subtitle_id': 9251120, ...  \n",
              "3  {'original_index': 0, 'subtitle_id': 9251120, ...  \n",
              "4  {'original_index': 0, 'subtitle_id': 9251120, ...  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3b8e165e-a8de-4cc4-b9bf-39fe20fb5aa8\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>chunk</th>\n",
              "      <th>metadata</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Watch any video online with OpenSUBTITLES Free...</td>\n",
              "      <td>{'original_index': 0, 'subtitle_id': 9251120, ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>on Keep dancing Whatever Im kidding Dont get m...</td>\n",
              "      <td>{'original_index': 0, 'subtitle_id': 9251120, ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>And you Douche Handsome Conceited Just like yo...</td>\n",
              "      <td>{'original_index': 0, 'subtitle_id': 9251120, ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>that so Yes How long will this program run If ...</td>\n",
              "      <td>{'original_index': 0, 'subtitle_id': 9251120, ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>her Gramps Uncle Erning Aunt Elma this is Tep ...</td>\n",
              "      <td>{'original_index': 0, 'subtitle_id': 9251120, ...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3b8e165e-a8de-4cc4-b9bf-39fe20fb5aa8')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-3b8e165e-a8de-4cc4-b9bf-39fe20fb5aa8 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-3b8e165e-a8de-4cc4-b9bf-39fe20fb5aa8');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-5608ccbb-f97a-4b61-a61a-eccf4f6abcea\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-5608ccbb-f97a-4b61-a61a-eccf4f6abcea')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-5608ccbb-f97a-4b61-a61a-eccf4f6abcea button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_sampled = df.sample(frac=0.30, random_state=42)"
      ],
      "metadata": {
        "id": "JidRG38HwVnf"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_sampled.info(memory_usage='deep')"
      ],
      "metadata": {
        "id": "lfPYYRqDwc7T",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "496c4ff8-ae33-46eb-bbe9-f6cb12f28d90"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Index: 466282 entries, 1320107 to 1294123\n",
            "Data columns (total 2 columns):\n",
            " #   Column    Non-Null Count   Dtype \n",
            "---  ------    --------------   ----- \n",
            " 0   chunk     466282 non-null  object\n",
            " 1   metadata  466282 non-null  object\n",
            "dtypes: object(2)\n",
            "memory usage: 338.8 MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_sampled.shape"
      ],
      "metadata": {
        "id": "-85J6681wzxO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "38dabae1-4c34-4848-8603-49337c53907f"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(466282, 2)"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Model name\n",
        "model_name = \"all-MiniLM-L6-v2\""
      ],
      "metadata": {
        "id": "BWn-w1HVw6wA"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sentence_transformers import SentenceTransformer\n",
        "import chromadb\n",
        "from chromadb.utils import embedding_functions\n",
        "import time\n",
        "import torch"
      ],
      "metadata": {
        "id": "MomIkhxMzo7d"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import torch\n",
        "from sentence_transformers import SentenceTransformer\n",
        "\n",
        "model = SentenceTransformer('all-MiniLM-L6-v2', device='cuda:0')\n",
        "\n",
        "sentences = [\"This is an example sentence\", \"Each sentence is converted\"]\n",
        "embeddings = model.encode(sentences, convert_to_tensor=True)\n",
        "\n",
        "print(embeddings.device) # should print cuda:0"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1ZKudpBZQKUf",
        "outputId": "caf0de4b-c04e-4af8-f141-8c0ba20fb82e"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.11/dist-packages/huggingface_hub/utils/_auth.py:94: UserWarning: \n",
            "The secret `HF_TOKEN` does not exist in your Colab secrets.\n",
            "To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.\n",
            "You will be able to reuse this secret in all of your notebooks.\n",
            "Please note that authentication is recommended but still optional to access public models or datasets.\n",
            "  warnings.warn(\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "cuda:0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def generate_embeddings(texts, model_name, batch_size=64, device=\"cuda:0\"):\n",
        "    \"\"\"Generates embeddings for a list of texts.\"\"\"\n",
        "    model = SentenceTransformer(model_name, device=device)\n",
        "    embeddings = model.encode(texts, batch_size=batch_size, show_progress_bar=True)\n",
        "    return embeddings"
      ],
      "metadata": {
        "id": "J5_HSmVNxUfa"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def store_embeddings_chroma(chunked_df, collection_name=\"subtitle_chunks\", persist_directory=\"./chroma_db\", batch_size=64):\n",
        "    \"\"\"Stores embeddings in ChromaDB with persistence.\"\"\"\n",
        "\n",
        "    start_time = time.time()  # Start time to measure performance\n",
        "\n",
        "    # Create or connect to the persistent ChromaDB client\n",
        "    client = chromadb.PersistentClient(path=persist_directory)\n",
        "\n",
        "    # Use the SentenceTransformer embedding function (ensure model_name is defined)\n",
        "    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)\n",
        "\n",
        "    try:\n",
        "        # Attempt to delete the existing collection if it exists\n",
        "        client.delete_collection(name=collection_name)\n",
        "    except ValueError:\n",
        "        pass  # Collection doesn't exist, so we continue\n",
        "\n",
        "    # Get or create the collection in ChromaDB\n",
        "    collection = client.get_or_create_collection(name=collection_name, embedding_function=embedding_function)\n",
        "\n",
        "    # Process the DataFrame in batches\n",
        "    for i in range(0, len(chunked_df), batch_size):\n",
        "        batch_df = chunked_df.iloc[i:i + batch_size]\n",
        "        texts = batch_df[\"chunk\"].tolist()  # Subtitle text for embeddings\n",
        "        metadatas = batch_df[\"metadata\"].tolist()  # Metadata (e.g., subtitle_id, name)\n",
        "        ids = [str(idx) for idx in batch_df.index.tolist()]  # Unique IDs for the documents\n",
        "\n",
        "        # Add the batch to the collection\n",
        "        collection.add(documents=texts, metadatas=metadatas, ids=ids)\n",
        "\n",
        "    # Measure and print time taken for the operation\n",
        "    end_time = time.time()\n",
        "    print(f\"Time taken to store embeddings: {end_time - start_time} seconds\")\n",
        "\n",
        "    return collection  # Return the collection for future use\n"
      ],
      "metadata": {
        "id": "tC0vEsTgyQQM"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def retrieve_and_display_results(query, collection, df, n_results=5, model_name=\"all-MiniLM-L6-v2\", device=\"cuda:0\"):\n",
        "    \"\"\"Retrieves top results and displays them with URLs.\"\"\"\n",
        "\n",
        "    # Initialize the SentenceTransformer model\n",
        "    model = SentenceTransformer(model_name, device=device)\n",
        "\n",
        "    # Get the query embedding\n",
        "    query_embedding = model.encode([query], show_progress_bar=False).tolist()\n",
        "\n",
        "    # Query the collection to retrieve top n results with metadata\n",
        "    results = collection.query(query_embeddings=query_embedding, n_results=n_results, include=[\"metadatas\"])\n",
        "\n",
        "    # Iterate over the results and print the details\n",
        "    for i, metadata in enumerate(results[\"metadatas\"][0]):\n",
        "        # Extract subtitle details from metadata (ensure keys exist in metadata)\n",
        "        subtitle_name = metadata.get(\"subtitle_name\", \"Unknown Subtitle\")\n",
        "        subtitle_id = metadata.get(\"subtitle_id\", \"Unknown ID\")\n",
        "\n",
        "        # Construct the OpenSubtitles URL\n",
        "        url = f\"https://www.opensubtitles.org/en/subtitles/{subtitle_id}\"\n",
        "\n",
        "        # Print the result details\n",
        "        print(f\"Result {i + 1}:\")\n",
        "        print(f\"  Subtitle Name: {subtitle_name.upper()}\")\n",
        "        print(f\"  URL: {url}\")\n",
        "        print(\"-\" * 20)\n"
      ],
      "metadata": {
        "id": "NmfWWUUlzVWR"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import warnings\n",
        "warnings.filterwarnings(\"ignore\")\n"
      ],
      "metadata": {
        "id": "6Y8Yybj_-YCa"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Example Usage\n",
        "persist_directory = r\"/content/drive/MyDrive/search_engine/db/\"\n",
        "# Store embeddings in ChromaDB\n",
        "collection = store_embeddings_chroma(df_sampled, persist_directory=persist_directory)\n",
        "\n"
      ],
      "metadata": {
        "id": "Mz-NBT_3zZg9"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import torch\n",
        "\n",
        "# Check if GPU is available and set the device\n",
        "device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n",
        "\n",
        "print(f\"Using device: {device}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7SWiSVEb_ZCQ",
        "outputId": "291ebe2c-8490-4f6d-c375-8e3c7c52f39a"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Using device: cuda\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Define your query\n",
        "query = \"what is the plan today?\"\n",
        "# Retrieve and display results\n",
        "retrieve_and_display_results(query=query, collection=collection, df=df_sampled, model_name=model_name, device=device) #uses the device defined at the top."
      ],
      "metadata": {
        "id": "roxU0tW0zdMq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "09afe0af-0121-4df2-f231-7026f9ac43f3"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result 1:\n",
            "  Subtitle Name: THE.MOSQUITO.COAST.S02.E03.TALK.ABOUT.THE.WEATHER.(2022).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9317090\n",
            "--------------------\n",
            "Result 2:\n",
            "  Subtitle Name: GRAND.CREW.S01.E07.WINE.HEADLINES.(2022).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9454011\n",
            "--------------------\n",
            "Result 3:\n",
            "  Subtitle Name: TULSA.KING.S01.E04.VISITATION.PLACE.(2022).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9340748\n",
            "--------------------\n",
            "Result 4:\n",
            "  Subtitle Name: I.AM.VANESSA.GUILLEN.(2022).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9316091\n",
            "--------------------\n",
            "Result 5:\n",
            "  Subtitle Name: THE.LONG.WAY.HOME.(1997).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9431169\n",
            "--------------------\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query = \"How is your day going\"\n",
        "retrieve_and_display_results(query=query, collection=collection, df=df_sampled, model_name=model_name, device=device)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RYPyXRxI-4Zh",
        "outputId": "84b0a13f-90cc-497c-f50a-bd904fd8c720"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result 1:\n",
            "  Subtitle Name: BACHELORETTES.DEGREE.(2013).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9189871\n",
            "--------------------\n",
            "Result 2:\n",
            "  Subtitle Name: THE.SILENT.TWINS.(2022).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9262310\n",
            "--------------------\n",
            "Result 3:\n",
            "  Subtitle Name: ONE.TREE.HILL.S08.E14.HOLDING.OUT.FOR.A.HERO.(2011).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9316729\n",
            "--------------------\n",
            "Result 4:\n",
            "  Subtitle Name: THIS.IS.US.S04.E15.CLOUDS.(2020).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9221613\n",
            "--------------------\n",
            "Result 5:\n",
            "  Subtitle Name: A.MAGICAL.CHRISTMAS.VILLAGE.(2022).ENG.1CD\n",
            "  URL: https://www.opensubtitles.org/en/subtitles/9301852\n",
            "--------------------\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "PCxo9hFs_3Oo"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
