
const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');

// The Dashboard sheet gid is usually 0 or something I found earlier.
// Wait, I can just check the mapClassDashboard function again to see what it uses.
