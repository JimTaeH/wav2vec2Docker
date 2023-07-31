# How to create simple API service for Wav2Vec2 model using FastAPI + Docker
This documentation demonstrates how to achieve an API service for a deep learning model. Which is rely on Hugging Face's Transformer library to load the processor and model. Let's get started!

## Prerequisite
We must install all of the following on the host machine to create API with docker and enable the GPU.
* [Docker](https://docs.docker.com/engine/install/) Select your OS and following the instruction.
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Nvidia Drivers](https://www.nvidia.com/download/index.aspx)
* [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#docker)
