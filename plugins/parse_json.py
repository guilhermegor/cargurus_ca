import json
import os
from typing import Dict, Any


class JsonFiles:

    def dump_message(self, message: Dict[str, Any], json_file: str) -> bool:
        with open(json_file, "w") as write_file:
            json.dump(message, write_file)
        if not os.path.exists(json_file):
            return False
        else:
            return True