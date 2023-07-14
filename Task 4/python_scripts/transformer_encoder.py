
import torch
from torch import nn

# Import relevant msa and mlp block scripts


try:
    import msa, mlp
except ImportError:
    print("[INFO] Cloning the repository and importing utils script...")
    subprocess.run(["git", "clone", "https://github.com/TalhaAhmed2000/DeepLearning.git"])
    subprocess.run(["mv", "DeepLearning/Task 4/python_scripts", "py_scripts"])
    sys.path.append('py_scripts')
    import msa, mlp

# 1. Create a class that inherits from nn.Module and implements all msa, mlp and residual connections all in one
class TransformerEncoderBlock(nn.Module):
    """Creates a Transformer Encoder block."""
    # 2. Initialize the class with hyperparameters from Table 1 and Table 3
    def __init__(self,
                 embedding_dim:int = 768, # Hidden size D from Table 1 for ViT-Base
                 num_heads:int = 12, # Heads from Table 1 for ViT-Base
                 mlp_size:int = 3072, # MLP size from Table 1 for ViT-Base
                 mlp_dropout:float = 0.1, # Amount of dropout for dense layers from Table 3 for ViT-Base
                 attn_dropout:float = 0): # Amount of dropout for attention layers
        super().__init__()

        # 3. Create MSA block (equation 2)
        self.msa_block = msa.MultiheadSelfAttentionBlock(embedding_dim = embedding_dim,
                                                     num_heads = num_heads,
                                                     attn_dropout = attn_dropout)

        # 4. Create MLP block (equation 3)
        self.mlp_block =  mlp.MLPBlock(embedding_dim = embedding_dim,
                                   mlp_size = mlp_size,
                                   dropout = mlp_dropout)

    # 5. Create a forward() method
    def forward(self, x):

        # 6. Create residual connection for MSA block (add the input to the output)
        x =  self.msa_block(x) + x

        # 7. Create residual connection for MLP block (add the input to the output)
        x = self.mlp_block(x) + x

        return x
