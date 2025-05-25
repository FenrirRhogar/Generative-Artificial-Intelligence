import torch

print(torch.version.cuda)  # Should return the CUDA version if supported
print(torch.cuda.is_available())  # Should return True if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"CUDA is available. Using device: {device}")
else:
    device = torch.device("cpu")
    print(f"CUDA is not available. Using device: {device}")