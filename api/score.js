/**
 * Vercel Serverless Function: /api/score
 * Fetch student score data directly from Potato English Google Sheet
 */

const SHEET_CSV_URL = 'https://docs.google.com/spreadsheets/d/1Z86AEyIs7yxSNzavuyRTCWz-PnD6xm8y06A-qPsGQR0/export?format=csv&gid=0';

let cachedCsv = null;
let lastCacheTime = 0;
const CACHE_TTL_MS = 60 * 1000; // 60 seconds in-memory cache

// Helper to parse CSV row handling quotes
function parseCsvLine(text) {
  const result = [];
  let cur = '';
  let inQuotes = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (c === '"') {
      if (inQuotes && text[i + 1] === '"') {
        cur += '"';
        i++;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (c === ',' && !inQuotes) {
      result.push(cur);
      cur = '';
    } else {
      cur += c;
    }
  }
  result.push(cur);
  return result;
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const queryId = (req.query.id || req.query.idScore || '').trim().toUpperCase();
  const testNum = parseInt(req.query.test || '1', 10) || 1;

  if (!queryId) {
    return res.status(400).json({ error: 'Missing parameter: id (ID Score)' });
  }

  try {
    const now = Date.now();
    let csvData = cachedCsv;

    if (!csvData || now - lastCacheTime > CACHE_TTL_MS) {
      const response = await fetch(SHEET_CSV_URL, {
        headers: { 'User-Agent': 'Potato-Score-API/1.0' }
      });
      if (!response.ok) {
        throw new Error(`Failed to fetch Google Sheet: ${response.statusText}`);
      }
      csvData = await response.text();
      cachedCsv = csvData;
      lastCacheTime = now;
    }

    const lines = csvData.split(/\r?\n/);
    if (lines.length < 3) {
      return res.status(500).json({ error: 'Sheet is empty or has no data rows' });
    }

    let foundRow = null;
    for (let i = 2; i < lines.length; i++) {
      const line = lines[i].trim();
      if (!line) continue;
      const cols = parseCsvLine(line);
      const rowId = (cols[0] || '').trim().toUpperCase();
      if (rowId === queryId) {
        foundRow = cols;
        break;
      }
    }

    if (!foundRow) {
      return res.status(404).json({
        found: false,
        error: `Không tìm thấy học viên với mã ID Score: ${queryId}`
      });
    }

    // Mapping based on Google Sheet structure:
    // Test 1: Date=Col 6, L=11, R=12, W=13, S=14, Total=15, Grade=16, SLink=17
    // Test 2: Date=Col 7, L=18, R=19, W=20, S=21, Total=22, Grade=23, SLink=24
    // Test 3: Date=Col 8, L=25, R=26, W=27, S=28, Total=29, Grade=30, SLink=31
    // Test 4: Date=Col 9, L=32, R=33, W=34, S=35, Total=36, Grade=37, SLink=38
    // Test 5: Date=Col 10, L=39, R=40, W=41, S=42, Total=43, Grade=44, SLink=45

    const getTestScores = (tIndex) => {
      const dateCol = 5 + tIndex; // 6 for Test 1, 7 for Test 2, etc.
      const baseCol = 11 + (tIndex - 1) * 7;
      return {
        testName: `Skill Test ${tIndex}`,
        date: foundRow[dateCol] || '',
        listening: foundRow[baseCol] || '',
        reading: foundRow[baseCol + 1] || '',
        writing: foundRow[baseCol + 2] || '',
        speaking: foundRow[baseCol + 3] || '',
        total: foundRow[baseCol + 4] || '',
        grade: foundRow[baseCol + 5] || '',
        speakingLink: foundRow[baseCol + 6] || ''
      };
    };

    const studentData = {
      found: true,
      idScore: foundRow[0] || queryId,
      classId: foundRow[1] || '',
      type: foundRow[2] || '',
      status: foundRow[3] || '',
      studentName: foundRow[4] || 'Học viên',
      teacher: foundRow[5] || '',
      selectedTest: getTestScores(testNum),
      allTests: {
        test1: getTestScores(1),
        test2: getTestScores(2),
        test3: getTestScores(3),
        test4: getTestScores(4),
        test5: getTestScores(5)
      },
      attitudes: {
        att1: foundRow[53] || 'Always / Luôn luôn', // BB: Pays attention
        att2: foundRow[54] || 'Usually / Đều đặn',  // BC: Volunteers & Participates
        att3: foundRow[55] || 'Always / Luôn luôn', // BD: Full attendance
        att4: foundRow[56] || 'Confident / Tự tin', // BE: Level of confidence
        att5: foundRow[59] || 'Usually well behaved / Tốt' // BH: Classroom Discipline
      },
      performance: {
        perf1: foundRow[61] || 'Competent / Khá tốt', // BJ: Speaking & Pronunciation
        perf2: foundRow[62] || 'Competent / Khá tốt', // BK: Reading & Vocabulary
        perf3: foundRow[63] || 'Competent / Khá tốt'  // BL: Listening Comprehension
      },
      comments: {
        teacherComment: foundRow[67] || '',
        suggestion: foundRow[66] || '',
        parentFeedback: foundRow[68] || ''
      }
    };

    return res.status(200).json(studentData);
  } catch (error) {
    console.error('Score API error:', error);
    return res.status(500).json({ error: 'Internal Server Error', message: error.message });
  }
}
