# NFTGuru

NFTGuru is a off-chain NFT valuation oracle allowing your NFTs to be used as collateral for DeFi.

Evaluates the model of each NFT owned by a wallet and deploys the valuation on the blockchain.
We use a valuation model which calculates the estimated value of an NFT based on the history of transactions of NFTs in the same collection with similar trait rarity. This model is serviced by an API (api.py), which is read by a oracle smart contract (NFToracle.sol). The NFTGuru web app loads the NFTs owned by an address, accessed by Metamask, and displays the NFTs, which can be evaluated by the model. Their values can be deployed to the blockchain to be used in DeFi apps.

# Todo:
 - Continuing to develop the model
 - Generalise oracle smart contract
