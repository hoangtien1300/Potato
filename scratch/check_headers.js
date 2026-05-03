
const spreadsheetId = '1dTcxPgSS2olUtgjjk2ZUvUo8e53Vi6J5Kk4bynKL0OE';
const gid = '1019913137';
const url = `https://docs.google.com/spreadsheets/d/${spreadsheetId}/export?format=csv&gid=${gid}`;

async function checkHeaders() {
    try {
        const response = await fetch(url);
        const csvText = await response.text();
        const headers = csvText.split('\n')[0];
        console.log("Headers:", headers);
        
        // Also show first row of data to see if it matches
        const firstRow = csvText.split('\n')[1];
        console.log("First row:", firstRow);
    } catch (error) {
        console.error("Error:", error);
    }
}

checkHeaders();
