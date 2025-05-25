import torch.nn as nn
import torch
import torch.nn.functional as F


class Decoder(nn.Module):
    def __init__(
        self,
        dims,
        dropout=None,
        dropout_prob=0.1,
        norm_layers=(),
        latent_in=(),
        weight_norm=True,
        use_tanh=True
    ):
        super(Decoder, self).__init__()

        ##########################################################
        # <================START MODIFYING CODE<================>
        ##########################################################
        # **** YOU SHOULD IMPLEMENT THE MODEL ARCHITECTURE HERE ****
        # Define the network architecture based on the figure shown in the assignment page.
        # Read the instruction carefully for layer details.
        # Pay attention that your implementation should include FC layers, weight_norm layers,
        # Leaky ReLU layers, Dropout layers and a tanh layer.
        self.input_dim = 3
        self.fc_layers = nn.Sequential(
            nn.Linear(self.input_dim, 512),
            nn.Linear(512, 512),
            nn.Linear(512, 512),
            nn.Linear(512, 509),
            nn.Linear(512, 512),
            nn.Linear(512, 512),
            nn.Linear(512, 512),
            nn.Linear(512, 1),
        )

        # Parametric Leaky ReLU 
        self.prelu = nn.LeakyReLU(negative_slope=0.2, inplace=True)

        # Dropout layer
        self.dropout_prob = dropout_prob
        self.dropout = nn.Dropout(dropout_prob) if dropout_prob > 0 else None

        # Tanh activation
        self.th = nn.Tanh() if use_tanh else None 

        for i in range(len(self.fc_layers) - 1):
            # Apply weight normalization for all layers except the last
            if weight_norm and i < len(self.fc_layers) - 1:
                self.fc_layers[i] = nn.utils.weight_norm(self.fc_layers[i]) if weight_norm else self.fc_layers[i]
        
        # ***********************************************************************
        ##########################################################
        # <================END MODIFYING CODE<================>
        ##########################################################
    
    # input: N x 3
    def forward(self, input):

        ##########################################################
        # <================START MODIFYING CODE<================>
        ##########################################################
        # **** YOU SHOULD IMPLEMENT THE FORWARD PASS HERE ****
        # Based on the architecture defined above, implement the feed forward procedure
        x = input
        # Pass through the first 4 FC layers (1st, 2nd, 3rd, 4th)
        for i in range(4):
            x = self.fc_layers[i](x)
            x = self.prelu(x)
            x = self.dropout(x)
                

        # Concatenate the 509-dim output with the 3-dim input
        x = torch.cat([x, input], dim=1)  # 512-dim

        # Pass through the next 3 FC layers (5th, 6th, 7th)
        for i in range(4, 7):
            x = self.fc_layers[i](x)
            x = self.prelu(x)
            x = self.dropout(x)

        # Pass through the last FC layer (8th)
        x = self.fc_layers[7](x)

        # Apply tanh activation
        x = self.th(x)
        # ***********************************************************************
        ##########################################################  
        # <================END MODIFYING CODE<================>
        ##########################################################

        return x
