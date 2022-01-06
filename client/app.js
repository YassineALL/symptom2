function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_symptom_names";

    $.get(url, function (data, status) {
        console.log("got response for get_symptome_names request");
        if (data) {
            var symptome = data.symptom;
            // $('#uiSymptoms').empty();
            // $('#uiSymptoms2').empty();
            for (var i in symptome) {
                var opt = new Option(symptome[i]);
                $('#uiSymptoms').append(opt);

            }
            for (var i in symptome) {
                var opt = new Option(symptome[i]);

                $('#uiSymptoms2').append(opt);
            }
            for (var i in symptome) {
                var opt = new Option(symptome[i]);

                $('#uiSymptoms3').append(opt);
            }
            for (var i in symptome) {
                var opt = new Option(symptome[i]);

                $('#uiSymptoms4').append(opt);
            }
            for (var i in symptome) {
                var opt = new Option(symptome[i]);

                $('#uiSymptoms5').append(opt);
            }
            for (var i in symptome) {
                var opt = new Option(symptome[i]);

                $('#uiSymptoms6').append(opt);
            }

        }
    });
}

window.onload = onPageLoad;






// function onClickedPredictDisease() {
//     console.log("Predict Diseases button clicked");
//
//     var s1 = document.getElementById("uiSymptoms").value;
//     var s2 = document.getElementById("uiSymptoms2").value;
//     var s3 = document.getElementById("uiSymptoms3").value;
//     var s4 = document.getElementById("uiSymptoms4").value;
//     var s5 = document.getElementById("uiSymptoms5").value;
//     var s6 = document.getElementById("uiSymptoms6").value;
//
//
//
//     var url2 = "http://127.0.0.1:5000/predict_disease";
//
//
//     $.post(url2, {
//
//         S1: s1,
//         S2: s2,
//         S3: s3,
//         S4: s4,
//         S5: s5,
//         S6: s6,
//     }, function (data, status) {
//
//             console.log(data.predict_disease);
//             $("#result").html(data.predict_disease);
//
//
//     });
// }
//

function onClickedPredictDisease() {
    console.log("Predict Diseases button clicked");

    var s1 = document.getElementById("uiSymptoms").value;
    var s2 = document.getElementById("uiSymptoms2").value;
    var s3 = document.getElementById("uiSymptoms3").value;
    var s4 = document.getElementById("uiSymptoms4").value;
    var s5 = document.getElementById("uiSymptoms5").value;
    var s6 = document.getElementById("uiSymptoms6").value;



    var url2 = "http://127.0.0.1:5000/predict_disease";
    var bodyToSend = {};
    if((s5 == "" || s5 == undefined) && s6 == "" || s6 == undefined){
        bodyToSend = {

            S1: s1,
            S2: s2,
            S3: s3,
            S4: s4,
        }
    }else if ((s6 == "" || s6 == undefined)){
        bodyToSend = {

            S1: s1,
            S2: s2,
            S3: s3,
            S4: s4,
            S5: s5,
        }
    }else{
        bodyToSend = {

            S1: s1,
            S2: s2,
            S3: s3,
            S4: s4,
            S5: s5,
            S6: s6,
        }
    }


    $.post(url2,bodyToSend , function (data, status) {

            console.log(data.predict_disease);
            $("#result").html(data.predict_disease);


    });
}