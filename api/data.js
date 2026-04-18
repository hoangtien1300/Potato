/**
 * AppSheet Proxy API Route for Vercel
 * This keeps the ApplicationAccessKey secure on the server.
 */

export default async function handler(req, res) {
    // Add CORS headers for local development
    res.setHeader('Access-Control-Allow-Credentials', true)
    res.setHeader('Access-Control-Allow-Origin', '*')
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT')
    res.setHeader(
        'Access-Control-Allow-Headers',
        'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
    )

    if (req.method === 'OPTIONS') {
        res.status(200).end()
        return
    }

    const { table } = req.query;
    
    // Environment variables (recommended to set in Vercel Dashboard)
    const appId = process.env.APPSHEET_APP_ID || '35e5f9f7-248a-4eb4-a87e-672f26329edc';
    const accessKey = process.env.APPSHEET_ACCESS_KEY || 'V2-ETGLA-CModK-89vqJ-sDZuU-PRMcH-y4WbA-429bw-9A60N';

    if (!table) {
        return res.status(400).json({ error: 'Table name is required' });
    }

    const url = `https://api.appsheet.com/api/v2/apps/${appId}/tables/${table}/Action`;

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'ApplicationAccessKey': accessKey,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                Action: 'Find',
                Properties: {
                    Locale: "en-US",
                    Timezone: "Asia/Bangkok"
                },
                Rows: []
            })
        });

        if (!response.ok) {
            const errorText = await response.text();
            return res.status(response.status).json({ 
                error: `AppSheet API Error: ${response.statusText}`,
                details: errorText 
            });
        }

        const data = await response.json();
        
        // Return data or empty array if null
        return res.status(200).json(data || []);
    } catch (error) {
        console.error('AppSheet Proxy Error:', error);
        return res.status(500).json({ error: 'Internal Server Error', message: error.message });
    }
}
