const fs = require('fs');
const path = require('path');

function convertValue(value) {
    if (typeof value === 'boolean') {
        return String(value).toLowerCase();
    }
    return value;
}

function encodeToCurl(inputFile, outputFile, baseUrl) {
    const jsonData = JSON.parse(fs.readFileSync(inputFile, 'utf8'));

    const params = Object.entries(jsonData)
        .map(([key, value]) => {
            const val = convertValue(value);
            return `${encodeURIComponent(key)}=${encodeURIComponent(
                typeof val === 'object' ? JSON.stringify(val) : val
            )}`;
        })
        .join('&');

    // Add headers here (modify as needed)
    const headers = {
        'Content-Type': 'text/csv',
        'x-api-key': '{{apiKey}}',
    };

    const headersStr = Object.entries(headers)
        .map(([key, value]) => `-H '${key}: ${value}'`)
        .join(' ');

    const curlCommand = `curl -X POST ${baseUrl}?${params} ${headersStr} --data-binary '@'`;

    fs.writeFileSync(outputFile, curlCommand);

    console.log(`Generated cURL command for ${inputFile}: ${outputFile}`);
}

// Process command line arguments
const program = path.basename(process.argv.at(1));
const args = process.argv.slice(2);
if (args.length < 2) {
    console.error(`Usage: node ${program} <input-file> <output-file>`);
    process.exit(1);
}

const inputFile = args[0];
const outputFile = args[1];
const baseUrl = 'https://apis.tollguru.com/toll/v2/gps-tracks-csv-upload';

encodeToCurl(inputFile, outputFile, baseUrl);

console.log('Conversion complete.');

