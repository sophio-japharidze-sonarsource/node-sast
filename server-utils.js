const Express = require("express");
const path = require("path");
const fs = require("fs/promises");

function createServer() {
  const app = Express();
  app.use(Express.urlencoded({ extended: true }));

  app.get("/", (_req, res) => {
    res.send("My second server!");
  });

  app.post("/", (req, res) => {
    const { dir } = req.body;
    const directory = path.join(__dirname, dir);
    fs.access(directory)
      .then(async () => {
        const result = await fs.readdir(directory);
        res.json({ files: result });
      })
      .catch(() => {
        res.json({ files: [] });
      });
  });

  return app;
}

module.exports = { createServer };
