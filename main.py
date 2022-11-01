import fastapi

import blockchain


bc = blockchain.BlockChain()
app = fastapi.FastAPI()


# endpoint to mine a block
@app.post("/api/v1/mine-block/")
def mine_block(data: str):
    if bc.is_chain_valid():
        block = bc.mine_block(data=data)
        return block

    return fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")


# endpoint to return entire blockchain
@app.get("/api/v1/blockchain/")
def get_blockchain():
    if bc.is_chain_valid():
        chain = bc.chain
        return chain

    return fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")


# endpoint to see if the chain is valid
@app.get("/api/v1/validate/")
def is_blockchain_valid():
    if bc.is_chain_valid():
        return bc.is_chain_valid()

    return fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")


# endpoint to return the last block
@app.get("/api/v1/blockchain/last/")
def previous_block():
    if bc.is_chain_valid():
        return bc.get_previous_block()

    return fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
