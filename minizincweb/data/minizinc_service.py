import os
from typing import Dict, Any

import minizinc


class MiniZincService:

    def solve(self, parameters: Dict[str, Any]) -> minizinc.Result:
        gecode = minizinc.Solver.lookup(
            os.environ["MINIZINC_SOLVER"] if "MINIZINC_SOLVER" in os.environ else "coin-bc"
        )
        model = minizinc.Model()
        model.add_string(self.read_model())
        instance = minizinc.Instance(gecode, model)

        for k, v in parameters.items():
            instance[k] = v

        return instance.solve()

    def read_model(self) -> str:
        with open(
                os.environ["MINIZINC_FILE"] if "MINIZINC_FILE" in os.environ else "solver.mzn",
                'r'
        ) as f:
            return f.read()
