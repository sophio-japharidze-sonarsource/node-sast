const Express = require("express");

const app = Express();
app.use(Express.urlencoded({ extended: true }));
const port = "3001";
const host = "localhost";

app.get("/search", (req, res) => {
  const { q } = req.query;
  res.send(`<html><body><h1>Search results for: ${q}</h1></body></html>`); // Noncompliant: XSS
});

app.listen(port, () => {
  console.log(`Server is running on http://${host}:${port}`);
});
