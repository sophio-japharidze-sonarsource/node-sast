const fs = require("fs");
const path = require("path");

function createDirectory(dirName) {
  const directory = path.join(__dirname, dirName);
  if (!fs.existsSync(directory)) {
    fs.mkdirSync(directory);
  } 
}

createDirectory(process.argv[2]);