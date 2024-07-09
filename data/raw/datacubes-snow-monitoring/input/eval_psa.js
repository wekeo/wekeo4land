//VERSION=3

function setup() {
    return {
        input: [
            { datasource: "psa", bands: ["PSA"] },
            { datasource: "asp", bands: ["aspect", "dem", "dataMask"] },
        ],
        output: {
            bands: 1,
            sampleType: "INT8"
        },
        mosaicking: "SIMPLE"
    }
}

// Altitude classes:
// Everything below the value will be returned in that key
var alt_class = Array(26).fill().map((element, index) => index * 100 + 1500)
// var alt_class = [1500, 2000, 2500, 3000, 3500, 4000]
var alt_names = Array(26).fill().map((element, index) => index * 100 + 1500)
alt_names.push(4500)

// Aspect classes
var asp_class = Array(8).fill().map((element, index) => index * 45 + 22.5)
var asp_names = Array(8).fill().map((element, index) => index * 45)
asp_names.push(0)
//var asp_names = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]

// Initialize statistics object for each aspect/altitude pair
var statistics = {}
for (var i = 0; i < alt_names.length; i++) {
    for (var j = 0; j < asp_names.length; j++) {
        let key = asp_names[j] + "_" + alt_names[i]
        statistics[key] = { "count": 0, "sum": 0 }
    }
}

var sample = 0;

function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
    outputMetadata.userData = statistics
}


function evaluatePixel(samples) {
    // Get values
    if (samples.asp[0].dataMask === 0) {
        return ([-1])
    }
    let aspect = samples.asp[0].aspect
    let psa = samples.psa[0].PSA
    let elevation = samples.asp[0].dem

    // Get correct interval
    let aspect_value = valueMap(aspect, asp_class, asp_names)
    let elev_value = valueMap(elevation, alt_class, alt_names)
    let key = aspect_value + "_" + elev_value

    //
    statistics[key]["count"]++
    if (psa === 1) {
        statistics[key]["sum"] += psa
        return [psa]
    }
    return [0]
}