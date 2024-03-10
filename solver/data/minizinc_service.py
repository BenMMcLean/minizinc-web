from typing import Dict, Any

import minizinc


class MiniZincService:

    def solve(self, parameters: Dict[str, Any]) -> minizinc.Result:
        gecode = minizinc.Solver.lookup("coin-bc")
        model = minizinc.Model()
        model.add_string(self.read_model())
        instance = minizinc.Instance(gecode, model)

        for k,v in parameters.items():
            instance[k] = v

        return instance.solve()

    def read_model(self) -> str:
        with open('./solver.mzn', 'r') as f:
            return f.read()
