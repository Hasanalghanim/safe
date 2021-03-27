setInterval(function(e){
    

    $.ajax({
        url:'dashboard/get',
        type: 'GET',
        dataType: '',
        success: function(data){
            $(".content-data").html(data),
            console.log('it work');
        },
        error: function(data){
            console.log('something went wrong');
        }
    });
}, 10000);         