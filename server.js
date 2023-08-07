const http = require("http");
const path = require("path");
const fs = require("fs/promises");

const port = "3000";
const host = "localhost";

const requestListener = function (req, res) {
  if (req.method === "POST") {
    let bodyChunks = [];
    req
      .on("data", (chunk) => {
        bodyChunks.push(chunk);
      })
      .on("end", () => {
        const body = Buffer.concat(bodyChunks).toString();
        const params = new URLSearchParams(body);
        const dir = params.get("dirName") || ".";
        const directory = path.join(__dirname, dir);
        res.setHeader("Content-Type", "application/json");
        res.writeHead(200);
        fs.access(directory)
          .then(async () => {
            const result = await fs.readdir(directory);
            res.end(JSON.stringify({ files: result }));
          })
          .catch(() => {
            res.end(JSON.stringify({ files: [] }));
          });
      });
  } else {
    res.writeHead(200);
    res.end("My first server!");
  }
};

const server = http.createServer(requestListener);
server.listen(port, () => {
  console.log(`Server is running on http://${host}:${port}`);
});
