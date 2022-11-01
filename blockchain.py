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
        proof = self._proof_of_work(
            data=data,
            index=index,
            prev_proof=prev_proof
        )
        prev_hash = self._hash(block=prev_block)
        block = self._create_block(
            data=data,
            index=index,
            proof=proof,
            prev_hash=prev_hash
        )
        self.chain.append(block)
        return block

    def _hash(self, block: dict) -> str:
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def _to_digest(self, data: str, new_proof: int, prev_proof: int, index: int) -> bytes:
        to_digest = str(new_proof ** 2 - prev_proof ** 2 + index) + data
        return to_digest.encode()

    def _proof_of_work(self, data: str, index: int, prev_proof: int) -> int:
        new_proof = 1
        check_proof = False
        while not check_proof:
            to_digest = self._to_digest(
                new_proof=new_proof,
                prev_proof=prev_proof,
                index=index,
                data=data,
            )
            hash_value = hashlib.sha256(to_digest).hexdigest()

            if hash_value[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1

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

    def is_chain_valid(self) -> bool:
        current_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            next_block = self.chain[block_index]

            if next_block.get("prev_hash") != self._hash(current_block):
                return False

            current_proof = current_block.get("proof")
            next_index, next_data, next_proof = (
                next_block.get("index"),
                next_block.get("data"),
                next_block.get("proof")
            )
            hash_value = hashlib.sha256(
                self._to_digest(
                    data=next_data,
                    new_proof=next_proof,
                    prev_proof=current_proof,
                    index=next_index
                )
            ).hexdigest()

            if hash_value[:4] != "0000":
                return False

            current_block = next_block
            block_index += 1

        return True
