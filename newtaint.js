const Express = require("express");
const path = require("path");
const fs = require("fs/promises");

const app = Express();
app.use(Express.urlencoded({ extended: true }));
const port = "3000";
const host = "localhost";


console.log(' iam here')
console.log(' iam here')
console.log(' iam here')
console.log(' iam here')
console.log(' iam here')
console.log(' iam here')
console.log(' iam here')
console.log(' iam here')
console.log(' iam here')
console.log(' iam here')

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

app.listen(3000, () => {
  console.log(`Server is running on http://${host}:${port}`);
});
