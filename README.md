# How to create simple API service for Wav2Vec2 model using FastAPI + Docker
This documentation demonstrates how to achieve an API service for a deep learning model. Which is rely on Hugging Face's Transformer library to load the processor and model. Let's get started!

## Prerequisite
We must install all of the following on the host machine to create API with docker and enable the GPU.
* [Docker](https://docs.docker.com/engine/install/) Select your OS and following the instruction.
* [Docker Compose](https://docs.docker.com/compose/install/) follow the instruction.
* [Nvidia Drivers](https://www.nvidia.com/download/index.aspx) Select your GPU and OS specification in the drop-down menu. Then download and install it following by instructions. But in case Windows OS + WSL2 with Ubuntu installed. You must install the Nvidia driver on your Windows system only. Don't install it in WSL2 because WSL2 basically sees the Nvidia driver in Windows.
* [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#docker) Follow this documentation (But you can skip that setting up docker because we already installed that.)
* [Download PyTorch (.whl) (Optional)](https://download.pytorch.org/whl/torch/) Because sometimes it has a network error when installing Torch which is a big file size. To fix it I recommend downloading the .whl file and installing from locally. (Version: torch-2.0.1+cu118-cp38-cp38-linux_x86_64.whl)

## Get Started
1. Clone this repository.
2. Move torch-2.0.1+cu118-cp38-cp38-linux_x86_64.whl into the root of cloned repository.
3. In docker-compose.yml change the path to your model and processor. The format of the model and processor must be loaded by Hugging Face's Transformer library. For more detailed sees [Fine-Tune Wav2Vec2](https://huggingface.co/blog/fine-tune-wav2vec2-english)
```console
version: '2.0'
services:
  w2v2xlsr53:
    build:
      context: .
      dockerfile: build/Dockerfile.engine
    image: n2nw2v2xlsr53
    # container_name: swt_webapp_messaging-engine
    volumes:
      - "PATH_TO_YOUR_MODEL_CHECKPOINT:/wav2vec2/model129hrs"
      - "PATH_TO_YOUR_PROCESSOR:/wav2vec2/processor"
    ports:
      - 5352:8000
```
