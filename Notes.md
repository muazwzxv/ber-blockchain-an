

# Blockchain
- At its core, blockchain is a distributed database that allows direct transactions between 2
	parties without the need of a middleman/auhtority

### Solution proposed by Satoshi Nakamoto
- A distributed ledgar :- a blockchain to keep track of all transactions in the network 

## Characteristic of Blockchain

### Distributed
- Ledgar is replicated accross number of computers, and not on a central server. Full copy of the
	blockchain can be downloaded 

### Cyptographic
- Used to make sure that the sender owns the bitcoin that she's trying to send, and can decide how
	the transaction is added to the blockchain

### Immutable
- Data on the network can only be changed by appending new block, which means can only be added nd
	not removed nor modified

### Proof of work
- Special participant in the network called miners compete on searching for the solution to a
	cryptographic puzzle that will allow them tto add a block of transactions to blockchain

## 2.1 Public key Cryptography

### Wallet
- public key :- info added to a block
- private key :- used to sign the transaction

### Hashing function and mining
- Transaction are group in files called blocks
- New blocks are added every 10 mins :- blocks added are immutable
- Special group of participant in the network called miners 
	- Bascially means computer connected to the network
	- Responsible creating new block of transaction
	- Has to authenticate each transacttion using the senders public key
		- Confirms that the sender has enough balance for the requested transaction
		- Add new transaction to the block
	- Also includes the transaction fee to incentivise the miners to add their transaction
- For the blocks to be accepted to the blockchain, it needs to be mined
- Miners need to find an extremely rare solution to a cryptographic puzzle :- process called Proof
	of work


