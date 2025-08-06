import torch
def main():
    print("PyTorch Version:", torch.__version__)
    print("CUDA Version:", torch.version.cuda)
    print("Is CUDA available?", torch.cuda.is_available())

if __name__ == "__main__":
    main()