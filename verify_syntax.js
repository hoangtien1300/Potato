
const fs = require('fs');

try {
    const content = fs.readFileSync('d:/02 POTATO English/Antigravity/Dashboard/Dashboard/index.html', 'utf8');
    const scriptMatch = content.match(/<script type="text\/babel">([\s\S]*?)<\/script>/);
    if (!scriptMatch) {
        console.log("No Babel script found.");
        process.exit(1);
    }
    const script = scriptMatch[1];
    
    // Very basic check for unbalanced braces
    let balance = 0;
    for (let i = 0; i < script.length; i++) {
        if (script[i] === '{') balance++;
        if (script[i] === '}') balance--;
        if (balance < 0) {
            console.log(`Unbalanced bracket at position ${i} (Line roughly ${script.substring(0, i).split('\n').length})`);
            // Find context
            console.log("Context: " + script.substring(i - 50, i + 50));
            // Don't exit yet, keep checking
        }
    }
    console.log("Final bracket balance:", balance);
    
    // Basic check for unclosed tags in JSX (naive)
    const openTags = (script.match(/<[a-zA-Z][a-zA-Z0-9]*/g) || []).length;
    const closeTags = (script.match(/<\/[a-zA-Z][a-zA-Z0-9]*/g) || []).length;
    const selfClosing = (script.match(/\/>/g) || []).length;
    console.log(`Tags - Open: ${openTags}, Close: ${closeTags}, Self-closing: ${selfClosing}`);
    console.log(`Expected Balance: ${openTags - closeTags - selfClosing}`);

} catch (e) {
    console.error(e);
}
