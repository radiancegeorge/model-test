const { spawn } = require("node:child_process");
const express = require("express");
const app = express();
const port = 3000;

app.use(express.json());
app.post("/", async (req, res) => {
  const { topic, essay } = req.body;
  const result = await new Promise((resolve, reject) => {
    const runPy = spawn("python3", [
      "-c",
      `from test import call_chat_completion; x = call_chat_completion("${topic}", "${essay}"); print(x)`,
    ]);
    runPy.stdout.on("data", (data) => {
      const r = data.toString();
      resolve(JSON.parse(r));
    });
    runPy.stderr.on("data", (data) => {
      console.log(`info: ${data}`);
    });

    runPy.on("close", (code) => {
      reject(`child process exited with code ${code}`);
    });
  }).catch(console.log);
  res.send(result);
});

app.listen(port, () => console.log("listening on port " + port));
