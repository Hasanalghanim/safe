// function walkTemplate(walkData) {
//     return `
//     <div class="row">
//         <div class="col s6 ">
//             <div class="card-panel teal">

//                 <h6> name: ${walkData.fields.name}</h6> <span> Call recived: ${walkData.fields.timerecived}</span>
//                 <h6> phone number:  ${walkData.fields.phone}</h6>
//                 <h6> From:  ${walkData.fields.fromlocation}</h6>
//                 <h6> to: ${walkData.fields.tolocation}</h6>
//             </div> 
//         </div>  
//     </div>  
//     `
// }

// setInterval(function () {


//     $.ajax({
//         url: 'dashboard/get',
//         type: 'GET',
//         data: "json",
//         dataType: 'json',
//         success: function (data) {
//             var i;
            
//             var data = data;
//             for (i = 0; i < data.length; i++){
//             document.getElementById("id_data").innerHTML = `
//             <h5 class="container center-align"> Pending Safewalk requests: ${data.length} </h5>
//             ${data.map(walkTemplate).join('')}



//             `   }
            
//         },
//         error: function () {
//             console.log('something went wrong');
//         }
//     });
// }, 5000);






