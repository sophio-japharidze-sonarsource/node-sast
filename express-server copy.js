const { createServer } = require("./server-utils");

const app = createServer();

app.listen(3002, () => {
  console.log("Server is running on http://localhost:3002");
});
