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

    def mine_block(self, data: str) -> dict:
        prev_block = self.get_previous_block()
        prev_proof = prev_block.get("proof")
        index = len(self.chain) + 1
        proof = None
        return {}

    def _proof_of_work(self, data: str, index: int, prev_proof: int) -> int:
        new_proof = 1
        check_proof = False
        while not check_proof:
            to_digest = False
        return new_proof

    def get_previous_block(self) -> dict:
        return self.chain[-1]

    def _create_block(self, data: str, proof: int, prev_hash: str, index: int) -> dict:
        block = {
            "index": index,
            "timestamp": str(datetime.datetime.now()),
            "data": data,
            "proof": proof,
            "prev_hash": prev_hash,
        }
        return block
