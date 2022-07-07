const imgPrc  = require("./prepare.image")
const { createWorker } = require('tesseract.js');

const imgUrl = "52616e646f6d4956a0e862652c64136faa0f4ebf0f821d925a4acd5e21fec7b2_rotated_cropped.jpeg"
const path = "/home/hanuman/Desktop/cards/" + imgUrl

const worker = createWorker();

(async () => {
    
    await worker.load();
    await worker.loadLanguage('eng');
    await worker.initialize('eng');

    const { data: { text } } = await worker.recognize(path);
    console.log(text);
    await worker.terminate();
})();