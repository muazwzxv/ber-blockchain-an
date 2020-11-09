

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

### Hashing and blockchain's cryptographic puzzle
- Hash function :- Any function that can be used to map data of arbitary size to data of fixed size,
	returns hashes
- cryptographic hash function allows one to easily verify that some input data maps to a given hash
	value
- A network like bitcoin uses SHA-256 and a number called nonce. By changing the block data or the
	nonce, we get completely different hashes
- Hash value of a block and nonce needs to meet a certain condiition
- Mining complexity increase by the added condition of hashes
- Miners has to find the nonce value that makes the hash value satisfies the mining condition


## 2.3 Linking blocks to Blockchain
- In order to create a chain of blockchains, each block uses the hash from the previous block's hash
	as part of its data
- Any changes to the data in any block will affect all the hash valus of he block after it and they
	will become invalid, this gives the blockchain its immutability characteristic

## 2.4 Adding blocks to the blockchain
- All miners compete with each other to find a valid block that will be added to the blockchain and
	get reward from the network
- Finding a nonce that validated block is rare
- But with the number of miners increased, adding a block to the blockchain is easy

### Resolving conflict 
- If 2 miners solve a block at the almost same time, 2 blocks will exist in the network, a new
	block is needed to solve this conflict
- Example
	- 2 blocks submitted { A, B }
	- If a new block is added on block A, Block B becoms invalid and vice versa

# Attacks on blockchain || Double spending

## Ways on performing a double spending attacks on the blockchain

### Race Attack
- Attacker spends the same coin in rapid succession to two different addresses
- To avoid this, it is recommended to wait at least one block confirmation before accepting the
	payment

### Finey Attack
- Attacker pre mines a block with a transactionm spends the same coins in a second transaction
	before releasing a block. The second transaction will not be validated. To prevent this,
	recommended to wait for at least 6 block confirmations before accepting the payment

### Majority attack || 51% attack
- Attacker owns 51% of the computing power of the network. The attackr starts by making a
	transaction that is brodcasted to the entire network, then mines a private blockchain where he
	double spends the coins of the previous transaction.
- Since the attacker owsn the majority of the computing power, he is guaranteed that he will have at
	some point a longer chain than the "honest" network. 




















