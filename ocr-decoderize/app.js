const CLIENT_ID = "2f8a8ec7-3cfd-4c1f-90a7-ed054d7cd245";
const API_KEY = "ZdxKILvlz1JmJg2ZTpJddgXlzin68ccVdxuL9NUw";
const API_HOST = "https://api.decoderize.cloud/v1";
const imageName = "01.jpeg";
const imageURL = `/home/hanuman/Desktop/cards-only-cover-pages/${imageName}`;

const fs = require("fs");
const axios = require("axios");

const imageToBase64 = (fileURI) => {
    const bitmap = fs.readFileSync(fileURI);
    return Buffer.from(bitmap).toString('base64');
};


const OCRStatuses = {
    NoUiidProvided: 0,
    Waiting: 1,
    Ready: 2,
    Unsuported: 3,
    Failed: 4
};


const OCRdecoderize = {
    sendImage: async (imageURL) => {
        try {
            const base64edImage = imageToBase64(imageURL);
            const response = await axios({
                method: 'POST',
                url: `${API_HOST}/upload-resource`,
                data: {
                    "clientId": CLIENT_ID,
                    "image": base64edImage
                },
                headers: {
                    "x-api-key": API_KEY
                }
            });

            if (response.data.OperationUuid)
                return response.data.OperationUuid;
            
            return null;
        }
        catch (err) {
            console.log(err);
            return null;
        }
    },
    checkResults: async (OperationUuid) => {
        if (!OperationUuid)
            return {
                data: null,
                status: OCRStatuses.NoUiidProvided
            };

        try {
            const response = await axios({
                method: 'POST',
                url: `${API_HOST}/processing-results`,
                data: {
                    "OperationUuid": OperationUuid,
                    "clientId": CLIENT_ID
                },
                headers: {
                    "x-api-key": API_KEY
                }
            });

            //console.log(response)
            //console.log(response.data)

            if (response.data.OperationStatus === "ProcessingFinished" && response.data.dataRecognitionResults.message === "Unsupported carrier or document type")
                return { status: OCRStatuses.Unsuported, data: null }

            if (response.data.OperationStatus === "ProcessingFinished")
                return { status: OCRStatuses.Ready, data: response.data.RecognitionResults }

            if (response.data.OperationStatus === "OpticalCharacterRecognitionInProgress")
                return { status: OCRStatuses.Waiting, data: null }

            return { status: OCRStatuses.Failed, data: null }

        }
        catch (err) {
            console.log(err);
            return {
                data: null,
                status: OCRStatuses.Failed
            };
        }
    }
};


(async () => {
    const uuid = await OCRdecoderize.sendImage(imageURL);
    if (!uuid) {
        console.log("no uuid provided")
        return;
    };

    const ocrData = await OCRdecoderize.checkResults(uuid)
    console.log(ocrData);
})()
