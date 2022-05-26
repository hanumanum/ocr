const imgPrc  = require("./prepare.image")
const { createWorker } = require('tesseract.js');

const worker = createWorker();


(async () => {
    
    const IMAGE_PATH = "images/2.jpg"
    await worker.load();
    await worker.loadLanguage('eng');
    await worker.initialize('eng');

    const { data: { text } } = await worker.recognize(IMAGE_PATH);
    console.log(text);
    await worker.terminate();
})();