import datetime
import hashlib
import json


class BlockChain:
    def __init__(self):
        self.chain = list()
        genesis_block = self._create_block(
            data="I'm a genesis block",
            proof=1,
            prev_hash="0",
            index=1
        )
        self.chain.append(genesis_block)

    def _create_block(self, data: str, proof: int, prev_hash: str, index: int) -> dict:
        block = {
            "index": index,
            "timestamp": str(datetime.datetime.now()),
            "data": data,
            "proof": proof,
            "prev_hash": prev_hash,
        }
        return block
