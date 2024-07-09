//VERSION=3

function setup() {
    return {
        input: ["PSA", "dataMask"],
        output: [
            {
                id: "persistent_snow",
                bands: 1
            },
            {
                id: "dataMask",
                bands: 1
            }
        ],
        mosaicking: "SIMPLE"
    }
}


function evaluatePixel(samples) {
    // Get values
    let dataMask = samples.dataMask
    let psa = samples.PSA
    if (psa > 1) {
        dataMask = 0
    }

    return {
        persistent_snow: [psa],
        dataMask: [dataMask]
    }
}