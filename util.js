function extractTitle(html) {
  const match = String(html).match(/<title\b[^>]*>([\s\S]*?)<\/title>/i);
  return match ? match[1] : null;
}

module.exports = {
  extractTitle,
};
