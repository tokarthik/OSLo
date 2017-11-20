var stats = {
    type: "GROUP",
name: "Global Information",
path: "",
pathFormatted: "group_missing-name-b06d1",
stats: {
    "name": "Global Information",
    "numberOfRequests": {
        "total": "6100",
        "ok": "2253",
        "ko": "3847"
    },
    "minResponseTime": {
        "total": "246",
        "ok": "246",
        "ko": "60000"
    },
    "maxResponseTime": {
        "total": "105721",
        "ok": "104778",
        "ko": "105721"
    },
    "meanResponseTime": {
        "total": "54628",
        "ok": "40152",
        "ko": "63105"
    },
    "standardDeviation": {
        "total": "17860",
        "ok": "21890",
        "ko": "5528"
    },
    "percentiles1": {
        "total": "60238",
        "ok": "43439",
        "ko": "61425"
    },
    "percentiles2": {
        "total": "62964",
        "ok": "57186",
        "ko": "64096"
    },
    "percentiles3": {
        "total": "70953",
        "ok": "70842",
        "ko": "71449"
    },
    "percentiles4": {
        "total": "84818",
        "ok": "81007",
        "ko": "85375"
    },
    "group1": {
        "name": "t < 800 ms",
        "count": 133,
        "percentage": 2
    },
    "group2": {
        "name": "800 ms < t < 1200 ms",
        "count": 18,
        "percentage": 0
    },
    "group3": {
        "name": "t > 1200 ms",
        "count": 2102,
        "percentage": 34
    },
    "group4": {
        "name": "failed",
        "count": 3847,
        "percentage": 63
    },
    "meanNumberOfRequestsPerSecond": {
        "total": "27.699",
        "ok": "10.23",
        "ko": "17.468"
    }
},
contents: {
"req_request-0-684d2": {
        type: "REQUEST",
        name: "request_0",
path: "request_0",
pathFormatted: "req_request-0-684d2",
stats: {
    "name": "request_0",
    "numberOfRequests": {
        "total": "6100",
        "ok": "2253",
        "ko": "3847"
    },
    "minResponseTime": {
        "total": "246",
        "ok": "246",
        "ko": "60000"
    },
    "maxResponseTime": {
        "total": "105721",
        "ok": "104778",
        "ko": "105721"
    },
    "meanResponseTime": {
        "total": "54628",
        "ok": "40152",
        "ko": "63105"
    },
    "standardDeviation": {
        "total": "17860",
        "ok": "21890",
        "ko": "5528"
    },
    "percentiles1": {
        "total": "60238",
        "ok": "43439",
        "ko": "61425"
    },
    "percentiles2": {
        "total": "62964",
        "ok": "57186",
        "ko": "64096"
    },
    "percentiles3": {
        "total": "70953",
        "ok": "70842",
        "ko": "71449"
    },
    "percentiles4": {
        "total": "84818",
        "ok": "81007",
        "ko": "85375"
    },
    "group1": {
        "name": "t < 800 ms",
        "count": 133,
        "percentage": 2
    },
    "group2": {
        "name": "800 ms < t < 1200 ms",
        "count": 18,
        "percentage": 0
    },
    "group3": {
        "name": "t > 1200 ms",
        "count": 2102,
        "percentage": 34
    },
    "group4": {
        "name": "failed",
        "count": 3847,
        "percentage": 63
    },
    "meanNumberOfRequestsPerSecond": {
        "total": "27.699",
        "ok": "10.23",
        "ko": "17.468"
    }
}
    }
}

}

function fillStats(stat){
    $("#numberOfRequests").append(stat.numberOfRequests.total);
    $("#numberOfRequestsOK").append(stat.numberOfRequests.ok);
    $("#numberOfRequestsKO").append(stat.numberOfRequests.ko);

    $("#minResponseTime").append(stat.minResponseTime.total);
    $("#minResponseTimeOK").append(stat.minResponseTime.ok);
    $("#minResponseTimeKO").append(stat.minResponseTime.ko);

    $("#maxResponseTime").append(stat.maxResponseTime.total);
    $("#maxResponseTimeOK").append(stat.maxResponseTime.ok);
    $("#maxResponseTimeKO").append(stat.maxResponseTime.ko);

    $("#meanResponseTime").append(stat.meanResponseTime.total);
    $("#meanResponseTimeOK").append(stat.meanResponseTime.ok);
    $("#meanResponseTimeKO").append(stat.meanResponseTime.ko);

    $("#standardDeviation").append(stat.standardDeviation.total);
    $("#standardDeviationOK").append(stat.standardDeviation.ok);
    $("#standardDeviationKO").append(stat.standardDeviation.ko);

    $("#percentiles1").append(stat.percentiles1.total);
    $("#percentiles1OK").append(stat.percentiles1.ok);
    $("#percentiles1KO").append(stat.percentiles1.ko);

    $("#percentiles2").append(stat.percentiles2.total);
    $("#percentiles2OK").append(stat.percentiles2.ok);
    $("#percentiles2KO").append(stat.percentiles2.ko);

    $("#percentiles3").append(stat.percentiles3.total);
    $("#percentiles3OK").append(stat.percentiles3.ok);
    $("#percentiles3KO").append(stat.percentiles3.ko);

    $("#percentiles4").append(stat.percentiles4.total);
    $("#percentiles4OK").append(stat.percentiles4.ok);
    $("#percentiles4KO").append(stat.percentiles4.ko);

    $("#meanNumberOfRequestsPerSecond").append(stat.meanNumberOfRequestsPerSecond.total);
    $("#meanNumberOfRequestsPerSecondOK").append(stat.meanNumberOfRequestsPerSecond.ok);
    $("#meanNumberOfRequestsPerSecondKO").append(stat.meanNumberOfRequestsPerSecond.ko);
}
