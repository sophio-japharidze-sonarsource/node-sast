const fs = require("fs");
const path = require("path");

function createDirectory(dirName) {
  const directory = path.join(__dirname, dirName);
  if (!fs.existsSync(directory)) {
    fs.mkdirSync(directory);
    const i = 0;
  } 
}

createDirectory(process.argv[2]);