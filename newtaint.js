const Express = require("express");

const app = Express();
app.use(Express.urlencoded({ extended: true }));
const port = "3002";
const host = "localhost";

app.post("/calculate", (req, res) => {
  const { expression } = req.body;
  const result = eval(expression); // Noncompliant: eval with user input
  res.json({ result });
});

app.listen(port, () => {
  console.log(`Server is running on http://${host}:${port}`);
});
