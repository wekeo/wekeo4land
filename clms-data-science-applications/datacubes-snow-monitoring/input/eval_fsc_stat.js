//VERSION=3

function setup() {
    return {
        input: ["GF", "dataMask"],
        output: [
            {
                id: "fractional_snow",
                bands: 1
            },
            {
                id: "dataMask",
                bands: 1
            }
        ],
        mosaicking: "TILE"
    }
}


function evaluatePixel(samples) {
    // Get values
    let snow = 0
    let valid = 0
    for (let i = 0; i < samples.length; i++) {
        if (samples[i].dataMask === 1) {
            valid = 1;
            if (samples[i].GF === 100) {
                snow = 1;
            }
        }
    }

    return {
        fractional_snow: [snow],
        dataMask: [valid]
    }
}