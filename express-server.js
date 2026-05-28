const { createServer } = require("./server-utils");

const app = createServer();

app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
