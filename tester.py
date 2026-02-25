import torch
print(f"Using device: {torch.device('cuda' if torch.cuda.is_available() else 'cpu')}")