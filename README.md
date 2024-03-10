# MiniZinc Web
*MiniZinc Web* provides a flask based HTTP wrapper around a MiniZinc instance and model.

## Usage
MiniZinc Web is primarily distributed as a Docker image, into which a model file should be mounted.
By default, the image loads `solver.mzn`, however different files can be loaded by setting the
`MINIZINC_FILE` environment variable. Likewise, the default solver is `coin-bc`, but an alternate
solver can be loaded by setting the `MINIZINC_SOLVER` environment variable. The flask server is
exposed through port 5000.

From there, the solver can be activated over HTTP by POSTing a JSON object to `/solve` in the form
```json
{
  "parameters": {
    <solver data here>
  }
}
```
which will return a response in the form of:
```json
{
  "status": <solve status>,
  "result": <json representation of minizinc output>
}
```

